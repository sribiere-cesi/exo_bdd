from behave import given, when, then

@given('un utilisateur enregistré avec l\'e-mail "{email}" et le mot de passe "{password}"')
def step_impl(context, email, password):
    context.email = email
    context.password = password

@when('il saisit "{email}" et "{password}"')
def step_impl(context, email, password):
    context.input_email = email
    context.input_password = password

@then('il est redirigé vers le tableau de bord')
def step_impl(context):
    assert context.input_email == context.email
    assert context.input_password == context.password
