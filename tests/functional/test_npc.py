import json



def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/npcs',
        data=json.dumps({
            'name': 'Zanzil the Outcast',
            'level': 46,
            'faction': 'Monster',
            'location': 'Stranglethorn Vale',
            'health': 1874,
            'damage': 128,
            'armor': 2255,
            'background': """Years ago, the Gurubashi exiled one of their own 
                from Zul'Gurub: a troll by the name of Zanzil. The reasons why 
                aren't all that clear, but it had most likely something to do with 
                Zanzils tendency to administer powerful, behavior-altering drugs to 
                anyone he saw. His mixtures cause those who drink it to become 
                strong but feeble-minded - similar to zombies.[3] Apparently, he 
                is the one troll too insane for the likes of the Gurubashi. Zanzil's 
                liberal use of Zanzil's Mixture has drugged just about everything 
                in the Ruins of Aboraz into obeying him, including naga, Chucky 
                "Ten Thumbs" and Yenniku. Yenniku was captured by Zanzil, who took 
                control of his body and mind, and then sent to the Skullsplitter 
                tribe to make them join him. Using a Soul Gem, players were able to 
                retrieve his soul."""
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'Zanzil the Outcast was added!' in data['message']