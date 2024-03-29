from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from email_validator import validate_email, EmailNotValidError

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Şifrə')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='Şifrəni təstiq edin')

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Şifrələr uyğun gəlmir!')
        if len(data['password1']) < 8:
            raise forms.ValidationError('Şifrənin uzunluğu ən az 8 simvol olmalıdır!')
        if data['password1'] != '\w':
            raise forms.ValidationError('Şifrənin daxilində hərf olmalıdır!')
        return data['password2']



class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Şifrə')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Bu adda istifadəçi mövcud deyil!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Yalnış şifrə daxil etmisiniz!')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('İstifadəçi aktiv deyil!')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserUpdateForm(forms.Form):
    # photo = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Şəkil')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Ad')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Soyad')
    # institution_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Müəssisə adı')

    class Meta:
        model = User
        fields = ('photo', 'first_name', 'last_name')
