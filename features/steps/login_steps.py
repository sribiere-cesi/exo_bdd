from behave import given, when, then

@given('un utilisateur enregistré avec l\'e-mail "{email}" et le mot de passe "{password}"')
def step_impl(context, email, password):
    context.email = email
    context.password = password


