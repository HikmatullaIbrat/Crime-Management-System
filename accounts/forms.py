
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ('email', 'full_name')

    def clean_password2(self):
        # check passwords matching
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    
    def save(self, commit=True):
        # Save password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """ A form for updating users. Includes all the fields on the user, but replaces the password field
    with admin's password hash display field. """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User

        # fields = ('full_name','email','password','active','admin')
        fields = ('full_name','email','password','admin')

    def clean_password(self):
        """Regardless of what the user provides, return the initial value. This is done here, rather    
        than on the field, because the field doesn't have access to the initial value.   """
        return self.initial['password']

# form after creating custom user model
class RegisterationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        # so after the creating a required field full_name we can add that field to forms
        # fields = ('email',)
        fields = ('email','full_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 !=  password2:
            raise forms.ValidationError("Password don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        # user.active = False  # Send confirmation email to check email exists or not, if active can log in
        if commit:
            user.save()
        return user 
