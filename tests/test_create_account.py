from playwright.sync_api import Page, expect

def test_create_account_without_birth_date(page:Page):
    print("Given the user visits the Create your account page")
    page.goto("https://www.ikea.com/es/es/profile/signup/family/")
    
    print("When the user fills in the first name field")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Nombre", exact=True).clear()
    page.get_by_role("textbox", name="Nombre", exact=True).fill("Edy")
    

    print("And the user fills in the last name field")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Apellido", exact=True).clear()
    page.get_by_role("textbox", name="Apellido", exact=True).fill("Guida")
    
    print("And the user selects the gender option")
    page.get_by_label("Sexo").select_option("FEMALE")
    
    print("And the user introduces the address")
    page.get_by_role("textbox", name="family-signup-form").click()
    page.get_by_role("textbox", name="family-signup-form").fill("28002")
    page.get_by_text("Calle de Aragón 28002 Madrid").click()
    page.locator("#family-signup-form-address-option-0").click()
    
    print("And the user selects the Favourite shop")
    page.get_by_label("Tienda preferida").select_option("665")
    
    print("And the user fills in the email address")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Correo electrónico (nombre de").clear()
    page.get_by_role("textbox", name="Correo electrónico (nombre de").fill("test@test.com")
    
    print("And the user fills in the password")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Contraseña").clear()
    page.get_by_role("textbox", name="Contraseña").fill("Test1234!")
    
    print("And the user accepts offers box")
    page.get_by_role("checkbox", name="Quiero recibir ofertas").check()
    
    print("And the user accepts privacy policy")
    page.get_by_role("checkbox", name="Confirmo que se me ha").check()
    page.get_by_role("checkbox", name="He leído y acepto las").check()
    
    print("And the user clicks on the Continue to verify button")
    page.get_by_role("button", name="Continuar para verificar").click()
    
    print("Then the user should see an error message and the account should not be created")
    expect(page.get_by_text("Tu fecha de nacimiento no es")).to_be_visible()

def test_create_account_without_email(page:Page):
    print("Given the user visits the Create your account page")
    page.goto("https://www.ikea.com/es/es/profile/signup/family/")
    
    print("When the user fills in the first name field")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Nombre", exact=True).clear()
    page.get_by_role("textbox", name="Nombre", exact=True).fill("Edy")
    

    print("And the user fills in the last name field")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Apellido", exact=True).clear()
    page.get_by_role("textbox", name="Apellido", exact=True).fill("Guida")

    print("And the user enters the date of birth")
    page.get_by_role("textbox", name="Fecha de nacimiento").click()
    page.get_by_role("textbox", name="Fecha de nacimiento").fill("16-09-1999")
    
    print("And the user selects the gender option")
    page.get_by_label("Sexo").select_option("FEMALE")
    
    print("And the user introduces the address")
    page.get_by_role("textbox", name="family-signup-form").click()
    page.get_by_role("textbox", name="family-signup-form").fill("28002")
    page.get_by_text("Calle de Aragón 28002 Madrid").click()
    page.locator("#family-signup-form-address-option-0").click()
    
    print("And the user selects the Favourite shop")
    page.get_by_label("Tienda preferida").select_option("665")
    
    print("And the user fills in the password")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Contraseña").clear()
    page.get_by_role("textbox", name="Contraseña").fill("Test1234!")
    
    print("And the user accepts offers box")
    page.get_by_role("checkbox", name="Quiero recibir ofertas").check()
    
    print("And the user accepts privacy policy")
    page.get_by_role("checkbox", name="Confirmo que se me ha").check()
    page.get_by_role("checkbox", name="He leído y acepto las").check()
    
    print("And the user clicks on the Continue to verify button")
    page.get_by_role("button", name="Continuar para verificar").click()

    print("Then the user should see an error message and the account should not be created")
    expect(page.get_by_text("El campo Correo electrónico (")).to_be_visible()

def test_create_account_under_18(page:Page):
    print("Given the user visits the Create your account page")
    page.goto("https://www.ikea.com/es/es/profile/signup/family/")
    
    print("When the user fills in the first name field")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Nombre", exact=True).clear()
    page.get_by_role("textbox", name="Nombre", exact=True).fill("Edy")
    

    print("And the user fills in the last name field")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Apellido", exact=True).clear()
    page.get_by_role("textbox", name="Apellido", exact=True).fill("Guida")

    print("And the user enters the date of birth that indicates that he´s under 18")
    page.get_by_role("textbox", name="Fecha de nacimiento").click()
    page.get_by_role("textbox", name="Fecha de nacimiento").fill("15-09-2024")
    
    print("And the user selects the gender option")
    page.get_by_label("Sexo").select_option("FEMALE")
    
    print("And the user introduces the address")
    page.get_by_role("textbox", name="family-signup-form").click()
    page.get_by_role("textbox", name="family-signup-form").fill("28002")
    page.get_by_text("Calle de Aragón 28002 Madrid").click()
    page.locator("#family-signup-form-address-option-0").click()
    
    print("And the user selects the Favourite shop")
    page.get_by_label("Tienda preferida").select_option("665")
    
    print("And the user fills in the email address")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Correo electrónico (nombre de").clear()
    page.get_by_role("textbox", name="Correo electrónico (nombre de").fill("test@test.com")
    
    print("And the user fills in the password")
    #We use the .clear to make sure the field is clear
    page.get_by_role("textbox", name="Contraseña").clear()
    page.get_by_role("textbox", name="Contraseña").fill("Test1234!")
    
    print("And the user accepts offers box")
    page.get_by_role("checkbox", name="Quiero recibir ofertas").check()
    
    print("And the user accepts privacy policy")
    page.get_by_role("checkbox", name="Confirmo que se me ha").check()
    page.get_by_role("checkbox", name="He leído y acepto las").check()
    
    print("And the user clicks on the Continue to verify button")
    page.get_by_role("button", name="Continuar para verificar").click()
    
    print("Then the user should see an error message and the account should not be created")
    expect(page.get_by_text("Debes tener 18-115 años.")).to_be_visible()