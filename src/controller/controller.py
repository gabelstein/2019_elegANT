from src.model.player import Player
from src.model.game_state import GameState
from src.view.view import View


class Controller:
    def __init__(self):
        self.player = Player()
        self.view = View(1300, 800)
        self.view.change_view_state(View.STARTVIEW)
        self.game_state = None

        self.event_list_start_view = {
            'start_button': self.start_button_pressed
        }

        self.event_list_game_view = {
            'build_scout': self.create_ant
        }
        self.game_loop()

    def start_button_pressed(self, color, player_name):
        self.view.change_view_state(View.GAMEVIEW)
        player = Player(color, player_name)
        player_list = [player]
        game_state = GameState(player_list)
       # print(player_name,color)
        return game_state

    def create_ant(self, nest_position, ant_amount):
        '''
        Function to create ant and nest for the first time if no nest assigned.
           Else assign the new ant to the available nest???
        '''
        self.game_state.create_ants(nest_position, ant_amount)

    def game_loop(self):
        i = 0
        while True:
            if self.game_state is None:
                self.view.draw()

                # Get the list of events from view
                # event_argument_list = self.view.get_event()
                event_argument_list = self.view.events()
                if event_argument_list:
                    print(event_argument_list)

                # Getting events and arguments as two lists
                event = list(event_argument_list.keys())
                args = list(event_argument_list.values())

                # Initializing player and game_state class
                for i in range(len(event)):
                    if event[i] in self.event_list_start_view.keys():
                        if args[i] is not None:
                            self.game_state = self.event_list_start_view[event[i]](*args[i])

            if self.game_state is not None:
                i += 1
                self.view.draw()
                self.view.events()

                # # Get the list of events from view
                # # event_argument_list = self.view.get_event()
                # event_argument_list = {}
                # if i == 10:
                #     event_argument_list = {'create_ant_button': ([10, 100], 1)}
                #
                # # Getting events and arguments as two lists
                # event = list(event_argument_list.keys())
                # args = list(event_argument_list.values())
                #
                # # Initializing player and game_state class
                # for i in range(len(event)):
                #     if event[i] in self.event_list_game_view.keys():
                #         if args[i] is not None:
                #             self.game_state = self.event_list_game_view[event[i]](*args[i])


if __name__ == "__main__":
    controller = Controller()
    controller.game_loop()
