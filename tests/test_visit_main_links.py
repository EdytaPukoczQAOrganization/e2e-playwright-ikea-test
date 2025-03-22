from playwright.sync_api import Page, expect
import os
import utils

def test_visit_main_menu_links_estancias_section(page:Page):
    print("Given the user visits the Ikea homepage")
    page.goto("https://www.ikea.com/es/es/")

    print("When the user accepts cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    #Close the popup, chosen Spain (Only happens on Github)
    if os.getenv("GITHUB_ACTIONS") == "true":
        page.get_by_role("button", name="España").click()

    if(utils.is_mobile(page) == True):

        #Mobile logic:
        print("And the user clicks on the Estancias tab(Mobile mode)")
        page.get_by_role("button", name="Menú").click()
        page.locator('a[href="https://www.ikea.com/es/es/rooms/"]').first.click()

    else:

        #Desktop logic:
        print("And the user clicks on the Estancias tab(Desktop mode)")
        page.get_by_role("tab", name="Estancias").click()


    #And the user clicks on the Dormitorio tab"
    if(utils.is_mobile(page) == True):

        #Mobile logic:
        print("And the user clicks on 'Dormitorio'")
        page.get_by_text("Dormitorio").first.click()

    else:

        #Desktop logic:
        page.locator("#hnf-carousel__tabs-navigation-rooms").get_by_role("link", name="Dormitorio").click()
    
        print("Then the user should be on the Dormitorio page")
        #We verify both url and the H1 element
        expect(page).to_have_url("https://www.ikea.com/es/es/rooms/bedroom/")
        expect(page.get_by_role("heading", name="Dormitorio", exact=True)).to_be_visible()

    
    #"Logic for going to 'Habitación infantil y juvenil'"
    if(utils.is_mobile(page) == True):

        #Mobile logic:
        print("And the user clicks on 'Habitación infantil y juvenil'")
        page.get_by_role("button", name="Menú").click()
        page.get_by_text("Habitación infantil y juvenil").first.click()
        
    else:

        #Desktop logic:
        print("And when the user clicks on the Estancias tab")
        page.get_by_role("tab", name="Estancias").click()
    
        print("And the user clicks on the Habitación infantil y juvenil tab")
        page.get_by_role("link", name="Habitación infantil y juvenil").click()
    
    print("Then the user should be on the Habitación infantil page")
    #We verify both url and the H1 element
    expect(page).to_have_url("https://www.ikea.com/es/es/rooms/childrens-room/")
    expect(page.get_by_role("heading", name="Habitación infantil")).to_be_visible()
    

    #"Logic for going to 'Salón'"
    if(utils.is_mobile(page) == True):

        #Mobile logic:
        print("And the user clicks on 'Salón'")
        page.get_by_role("button", name="Menú").click()
        page.get_by_text("Salón").first.click()
        
    else:

        #Desktop logic:
        print("And when the user clicks on the Estancias tab")
        page.get_by_role("tab", name="Estancias").click()
    
        print("And the user clicks on the Salón tab")
        page.get_by_role("link", name="Salón").click()
    

    print("Then the user should be on the Salón page")
    #We verify both url and the H1 element
    expect(page).to_have_url("https://www.ikea.com/es/es/rooms/living-room/")
    expect(page.get_by_role("heading", name="Salón", exact=True)).to_be_visible()
