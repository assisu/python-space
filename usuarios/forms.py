from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,  
        widget=forms.TextInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Ex: Joao silva"
                    }
                )
    )

    senha=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Ex: Digite sua senha"
                    }
                )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,  
        widget=forms.TextInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Ex: Joao silva"
                    }
                )
    )

    email=forms.EmailField(
        label='Email', 
                required=True, 
                max_length=70,
                widget=forms.EmailInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Ex: joaosilva@xpto.com"
                    }
                )
    )
    senha_1=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Ex: Digite sua senha"
                    }
                )
    )
    senha_2=forms.CharField(
                label='Repita a senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Ex: Digite sua senha novamente"
                    }
                )
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços no campo nome de cadastro")
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("A senhas não são iguais")
            else: 
                return senha_2


   