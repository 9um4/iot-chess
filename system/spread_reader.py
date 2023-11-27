from oauth2client.service_account import ServiceAccountCredentials
import gspread

class Spread_Reader:

    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
        ]

    def __init__(self, key_file: str) -> None:
        self.key_file = key_file
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key_file, Spread_Reader.scope)
        self.sheet = gspread.authorize(self.credentials).open('iot-chess').worksheet('input')
        self.first_player = {}
        self.second_player = {}
        self.update_data(1)
        self.update_data(2)

    def update_data(self, index: int) -> None:
        if (index == 1):
            first_player_data = [value for row in self.sheet.get('B2:B8') for value in row]
            if first_player_data:
                self.first_player = {
                    "id": first_player_data[0],
                    "name": first_player_data[1],
                    "state": first_player_data[2],
                    "piece": first_player_data[3],
                    "location_x": int(first_player_data[4]),
                    "location_y": int(first_player_data[5]),
                    "command": int(first_player_data[6])
                }
            print(self.first_player)
        elif (index == 2):
            second_player_data = [value for row in self.sheet.get('G2:G8') for value in row]
            if second_player_data:
                self.second_player = {
                    "id": second_player_data[0],
                    "name": second_player_data[1],
                    "state": second_player_data[2],
                    "piece": second_player_data[3],
                    "location_x": int(second_player_data[4]),
                    "location_y": int(second_player_data[5]),
                    "command": int(second_player_data[6])
                }

    def get_value(self, sheet_name: str, location: str):
        return self.sheet.acell(location).value
    
    def set_value(self, sheet_name: str, location: str, value: str):
        self.sheet.update(location, value)

    def player_exists(self, index: int) -> bool:
        if (index == 1):
            return self.get_value('input', 'B2') != None
        if (index == 2):
            return self.get_value('input', 'G2') != None
        return False

    def get_id(self, index: int) -> int:
        if (index == 1 and self.player_exists(1)):
            return int(self.get_value('input', 'B2'))
        elif (index == 2 and self.player_exists(2)):
            return int(self.get_value('input', 'G2'))
        return -1
    
    def set_id(self, index: int, id: int) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B2', str(id))
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G2', str(id))
        return -1

    def get_name(self, index: int) -> str:
        if (index == 1 and self.player_exists(1)):
            return self.get_value('input', 'B3')
        elif (index == 2 and self.player_exists(2)):
            return self.get_value('input', 'G3')
        return None
    
    def set_name(self, index: int, name: str) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B3', name)
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G3', name)
        return -1
    
    def get_state(self, index: int) -> str:
        if (index == 1 and self.player_exists(1)):
            return self.get_value('input', 'B4')
        elif (index == 2 and self.player_exists(2)):
            return self.get_value('input', 'G4')
        return None
    
    def set_state(self, index: int, state: str) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B4', state)
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G4', state)
        return -1
    
    def get_piece(self, index: int) -> int:
        if (index == 1 and self.player_exists(1)):
            return self.get_value('input', 'B5')
        elif (index == 2 and self.player_exists(2)):
            return self.get_value('input', 'G5')
        return None
    
    def set_piece(self, index: int, piece: str) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B5', piece)
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G5', piece)
        return -1

    def get_location_x(self, index: int) -> int:
        if (index == 1 and self.player_exists(1)):
            return self.get_value('input', 'B6')
        elif (index == 2 and self.player_exists(2)):
            return self.get_value('input', 'G6')
        return None
    
    def set_location_x(self, index: int, location_x: int) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B6', location_x)
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G6', location_x)
        return -1
    
    def get_location_y(self, index: int) -> int:
        if (index == 1 and self.player_exists(1)):
            return self.get_value('input', 'B7')
        elif (index == 2 and self.player_exists(2)):
            return self.get_value('input', 'G7')
        return None
    
    def set_location_y(self, index: int, location_y: int) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B7', location_y)
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G7', location_y)
        return -1
    
    def get_command(self, index: int) -> int:
        if (index == 1 and self.player_exists(1)):
            return self.get_value('input', 'B8')
        elif (index == 2 and self.player_exists(2)):
            return self.get_value('input', 'G8')
        return None
    
    def set_command(self, index: int, command: int) -> None:
        if (index == 1 and self.player_exists(1)):
            self.set_value('input', 'B8', command)
        elif (index == 2 and self.player_exists(2)):
            self.set_value('input', 'G8', command)
        return -1

    def update_first_player(
            self,
            ) -> None:
        print(self.first_player)
        values = [
            self.first_player['id'],
            self.first_player['name'],
            self.first_player['state'],
            self.first_player['piece'],
            self.first_player['location_x'],
            self.first_player['location_y'],
            self.first_player['command']
            ]
        print(values)
        self.sheet.update('B2:B8', [[value] for value in values]
            )
        
    def update_second_player(
            self,
            ) -> None:
        values = [
            self.second_player['id'],
            self.second_player['name'],
            self.second_player['state'],
            self.second_player['piece'],
            self.second_player['location_x'],
            self.second_player['location_y'],
            self.second_player['command']
            ]
        print(values)
        self.sheet.update('G2:G8', [[value] for value in values]
            )
        
    def register_first_player(
            self,
            id: int,
            name: str,
            state: str,
            piece: str,
            location_x: int = 0,
            location_y: int = 0,
            command: str = None
            ) -> bool:
        if (not self.player_exists(1)):
            self.update_first_player()
            return True
        return False
    
    def register_second_player(
            self,
            id: int,
            name: str,
            state: str,
            piece: str,
            location_x: int = 0,
            location_y: int = 0,
            command: str = None
            ) -> bool:
        if (not self.player_exists(2)):
            self.update_second_player()
            return True
        return False
    

if __name__ == "__main__":
    sr = Spread_Reader("D:\.python\.iot\iot-chess\.credentials\key.json")
    sr.set_id(1, 1)