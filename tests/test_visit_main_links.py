from playwright.sync_api import Page, expect

def test_visit_main_menu_links_estancias_section(page:Page):
    print("Given the user visits the Ikea homepage")
    page.goto("https://www.ikea.com/es/es/")

    print("When the user accepts cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    #Close the popup, chosen Spain (Only happens on Github)
    page.get_by_role("button", name="España").click()

    print("And the user clicks on the Estancias tab")
    page.get_by_role("tab", name="Estancias").click()
    
    print("And the user clicks on the Dormitorio tab")
    page.locator("#hnf-carousel__tabs-navigation-rooms").get_by_role("link", name="Dormitorio").click()
    
    print("Then the user should be on the Dormitorio page")
    #We verify both url and the H1 element
    expect(page).to_have_url("https://www.ikea.com/es/es/rooms/bedroom/")
    expect(page.get_by_role("heading", name="Dormitorio", exact=True)).to_be_visible()

    print("And when the user clicks on the Estancias tab")
    page.get_by_role("tab", name="Estancias").click()
    
    print("And the user clicks on the Habitación infantil y juvenil tab")
    page.get_by_role("link", name="Habitación infantil y juvenil").click()
    
    print("Then the user should be on the Habitación infantil page")
    #We verify both url and the H1 element
    expect(page).to_have_url("https://www.ikea.com/es/es/rooms/childrens-room/")
    expect(page.get_by_role("heading", name="Habitación infantil")).to_be_visible()
    
    print("And when the user clicks on the Estancias tab")
    page.get_by_role("tab", name="Estancias").click()
    
    print("And the user clicks on the Salón tab")
    page.get_by_role("link", name="Salón").click()
    
    print("Then the user should be on the Salón page")
    #We verify both url and the H1 element
    expect(page).to_have_url("https://www.ikea.com/es/es/rooms/living-room/")
    expect(page.get_by_role("heading", name="Salón", exact=True)).to_be_visible()
