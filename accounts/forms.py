from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Esse usuario não existe")
            if not user.check_password(password):
                raise forms.ValidationError("Essa senha não é correta")
            if not user.is_active:
                raise forms.ValidationError("Usuário não ativo")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Endereço de Email")
    password = forms.CharField(widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password']
    


    
