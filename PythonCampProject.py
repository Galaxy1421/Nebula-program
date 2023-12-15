import requests
from PIL import Image

print('\n.*°٠⟡˚₊ Hello, my name is Ghaida Al-Essa. I call myself Galaxy. I am an astrophile, so I chose this simple idea about my favorite nebulas .*°٠⟡˚₊\n')
def display_nebula_info_with_image(nebula_name, ngc_number, distance_light_years, diameter_light_years, constellation, image_url):
    """
    Display information about a specific nebula along with an image from the internet.

    """
    print('Information about Nebula (', ngc_number, '): ', nebula_name,)
    print('Distance from Earth: ', distance_light_years, 'light years')
    print('Diameter: ', diameter_light_years, ' light years')
    print('Located in Constellation: ', constellation)


    response = requests.get(image_url, stream=True)
    response.raise_for_status()


    image = Image.open(response.raw)
    image.show()


nebula_choices = {
    "1": ("Butterfly Nebula", "NGC 6302", 3800, 0.8, "Scorpius", "https://www.nasa.gov/wp-content/uploads/2023/03/754349main_butterfly_nebula_full_full.jpg"),
    "2": ("Antennae Galaxies", "NGC 4038/4039", 60, 120, "Corvus", "https://www.eso.org/public/archives/images/screen/eso1137f.jpg"),
    "3": ("Helix Nebula", "NGC 7293", 700, 2.5, "Aquila", "https://www.eso.org/public/archives/images/screen/eso0907b.jpg"),
    "4": ("Cat's Eye Nebula", "NGC 6543", 3300, 0.6, "Draco", "https://www.nasa.gov/wp-content/uploads/2023/03/64884main_image_feature_211_jwfull.jpg"),
    "5": ("Crab Nebula", "NGC 1952", 6500, 11, "Taurus", "https://stsci-opo.org/STScI-01EVT1F4GCP2K6PFZJVHYCAC3N.png"),
}


print("List of my favorite nebulae: ")
for key, (name, ngc, _, _, _, _) in nebula_choices.items():
    print(f"{key}. {name} ({ngc})")


user_choice = input("Choose one to explore: ")


selected_nebula = nebula_choices.get(user_choice)
if selected_nebula:
    display_nebula_info_with_image(*selected_nebula)
else:
    print("Invalid choice. Please select a valid number from the list.")
