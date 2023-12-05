from playwright.sync_api import Page, expect


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tag = page.locator("article")
    expect(div_tag).to_have_text(
        ["Demon Days Released: 2005", "Doolittle Released: 1989"]
    )


def test_get_album_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    expect(page.locator("h1")).to_have_text("Demon Days")
    expect(page.locator("p")).to_have_text("Release year: 2005")


# test individual album page
def test_visit_album_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Demon Days")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Demon Days")
