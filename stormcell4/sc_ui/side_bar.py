import pygame

from StormCell.stormcell4.sc_ui.label import Label
from StormCell.stormcell4.sc_ui.sc_container import SCContainer, ContainerOrientation
from StormCell.stormcell4.sc_ui.sc_image import SCImage

NATION_GOV_TYPE="Imperial Despotism"

class SideBar():
    def __init__(self, location, size):
        self.size=size
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location)

    def draw(self, screen, game):
        self.surface.fill(pygame.Color('white'))
        # self.surface.blit(self.txt_surf, self.txt_rect)

        emblem = SCImage(
            image_path="/Users/brendanritter/fun/StormCell/stormcell4/resources/images/spearhead.png",
            size=(52, 60),
            border_size=5,
            border_color='#E80755',
        )

        country_title_text=Label(game.playing_as_country.name,font_size=20)
        country_title_text.update()

        country_type_text=Label(NATION_GOV_TYPE,font_size=16)
        country_type_text.update()

        religion_icon = SCImage(
            image_path="/Users/brendanritter/fun/StormCell/stormcell4/resources/images/censer.png",
            size=(25, 30),
        )

        gov_type_and_religion_icon=SCContainer(
            [country_type_text,religion_icon]
        )

        country_title_and_else=SCContainer(
            [country_title_text,gov_type_and_religion_icon],
            orientation=ContainerOrientation.VERTICAL
        )
        emblem_and_else=SCContainer([emblem,country_title_and_else])

        resources=["a","b","c","d","e"]
        resource_boxes=[]
        for i,resource in enumerate(resources):
            resource_amnt=Label(str(i))
            resource_icon=SCImage(
                image_path=f"/Users/brendanritter/fun/StormCell/stormcell4/resources/images/{resource}.png",
                size=(20, 20)
            )
            resource_and_icon=SCContainer([resource_amnt,resource_icon],inner_padding=5)
            resource_boxes.append(resource_and_icon)

        resources = SCContainer(resource_boxes,inner_padding=15)
        top_and_resources = SCContainer([emblem_and_else,resources],orientation=ContainerOrientation.VERTICAL, inner_padding=15)

        self.selected_tile_label = Label("", font_size=20)
        country_info_and_selected = SCContainer([top_and_resources,self.selected_tile_label], orientation=ContainerOrientation.VERTICAL,inner_padding=15)

        country_info_and_selected.draw(self.surface,(0,0))

        # censer_img = pygame.image.load("/Users/brendanritter/fun/StormCell/stormcell4/resources/images/censer.png").convert_alpha()
        # censer_img = pygame.transform.scale(censer_img, (25, 30))
        # self.surface.blit(censer_img, (250, 30))


        # img = pygame.image.load("/Users/brendanritter/fun/StormCell/stormcell4/resources/images/spearhead.png").convert_alpha()
        # img = pygame.transform.scale(img, (52, 60))
        # # pygame.draw.rect(self.surface,'#E80755',pygame.Rect(0,0,62,70))
        # # self.surface.blit(img, (5, 5))
        # #
        # country_title_text=Label(game.playing_as_country.name,(65,0),font_size=20)
        # country_title_text.update()
        # # country_title_text.draw(self.surface,(65,0))
        #
        # country_type_text=Label(NATION_GOV_TYPE,(65,30),font_size=16)
        # country_type_text.update()
        # country_type_text.draw(self.surface)

        # herp=SCContainer([country_title_text,country_type_text])
        #
        # print(country_title_text.get_size())
        # print(herp.get_size())
        #
        # herp.draw(self.surface,(0,0))

        #
        # censer_img = pygame.image.load("/Users/brendanritter/fun/StormCell/stormcell4/resources/images/censer.png").convert_alpha()
        # censer_img = pygame.transform.scale(censer_img, (25, 30))
        # self.surface.blit(censer_img, (250, 30))
        #
        screen.blit(self.surface, self.rect)

    def get_selected_tile_widget(self):
        return self.selected_tile_label