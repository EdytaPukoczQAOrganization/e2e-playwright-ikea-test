from playwright.sync_api import Page, expect
import re

def test_search_valid_value(page:Page):
    print("Given the user is on the Ikea homepage")
    page.goto("https://www.ikea.com/es/es/")
    
    print("When the user accepts cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    print("And the user introduces a valid search value silla")
    #We use the .clear option to clear the search box in case there was something in there before
    ##page.get_by_role("combobox", name="Buscar por producto,").clear()
    page.get_by_placeholder("Qué es lo que buscas").click()
    ##page.get_by_role("combobox", name="Buscar por producto,").fill("silla")
    page.get_by_placeholder("Qué es lo que buscas").fill("silla")
    
    print("And the user hits enter")
    ##page.get_by_role("button", name="Buscar").click()
    ##page.get_by_role("tooltip", name="Buscar").click()
    page.locator("span").filter(has_text=re.compile(r"^Buscar$")).click()
    


    
    print("Then the user should see the search results with the search term silla as the H1")
    expect(page.locator("h1")).to_contain_text("silla")

def test_search_empty_value(page:Page):
    print("Given the user is on the Ikea homepage")
    page.goto("https://www.ikea.com/es/es/")
    
    print("When the user accepts cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    print("And the user introduces an empty value and press enter")

    page.get_by_role("combobox", name="Buscar por producto,").click()
    ##page.get_by_role("combobox", name="Buscar por producto,").press("Enter")
    page.get_by_placeholder("Qué es lo que buscas").fill(" ")
    page.locator("span").filter(has_text=re.compile(r"^Buscar$")).click()
    
    print("Then the user should still be seeing the search box with Buscar por producto text")
    expect(page.get_by_role("combobox", name="Buscar por producto,")).to_be_visible()
  