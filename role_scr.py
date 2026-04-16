from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from random import shuffle

class RoleScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.current_player_index = 0
        self.roles = []
        
        # Основной layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Метка для отображения номера игрока
        self.player_label = Label(text='Игрок 1', font_size='20sp', size_hint=(1, 0.2))
        
        # Метка для отображения роли
        self.role_label = Label(text='Нажмите кнопку', font_size='30sp', color=(1, 1, 0, 1), size_hint=(1, 0.5))
        
        # Кнопка показа роли
        self.show_button = Button(text='Показать карту', font_size='18sp', size_hint=(1, 0.15))
        self.show_button.on_press = self.show_role
        
        # Кнопка перехода к следующему игроку (изначально скрыта)
        self.next_button = Button(text='Далее →', font_size='18sp', size_hint=(1, 0.15))
        self.next_button.on_press = self.next_player
        self.next_button.opacity = 0
        self.next_button.disabled = True
        
        layout.add_widget(self.player_label)
        layout.add_widget(self.role_label)
        layout.add_widget(self.show_button)
        layout.add_widget(self.next_button)
        
        self.add_widget(layout)

    def on_pre_enter(self, *args):
        """Вызывается перед показом экрана"""
        app = App.get_running_app()
        
        # Создаем список ролей
        self.roles = []
        
        # Добавляем мирных
        for i in range(app.peaceful_count):
            self.roles.append('Мирный')
        
        # Добавляем мафию
        for i in range(app.mafia_count):
            self.roles.append('Мафия')
        
        # Добавляем доктора
        for i in range(app.doctor_count):
            self.roles.append('Доктор')
        
        # Добавляем путану
        for i in range(app.prostitute_count):
            self.roles.append('Путана')
        
        # Добавляем комиссара
        for i in range(app.comisar_count):
            self.roles.append('Комиссар')
        
        # Перемешиваем роли
        shuffle(self.roles)
        
        # Сбрасываем счетчик игроков
        self.current_player_index = 0
        
        # Сбрасываем интерфейс
        self.role_label.text = 'Нажмите кнопку'
        self.role_label.color = (1, 1, 0, 1)
        self.show_button.opacity = 1
        self.show_button.disabled = False
        self.next_button.opacity = 0
        self.next_button.disabled = True
        
        # Обновляем номер игрока
        self.update_player_label()
        
        print(f"Созданы роли: {self.roles}")  # Для отладки

    def update_player_label(self):
        """Обновляет метку с номером текущего игрока"""
        total_players = len(self.roles)
        self.player_label.text = f'Игрок {self.current_player_index + 1} из {total_players}'

    def show_role(self):
        """Показывает роль текущего игрока"""
        if self.current_player_index < len(self.roles):
            role = self.roles[self.current_player_index]
            
            # Настройка цвета и текста в зависимости от роли
            if role == 'Мафия':
                self.role_label.color = (1, 0, 0, 1)  # Красный
                role_text = f'Твоя роль: {role} '
            elif role == 'Доктор':
                self.role_label.color = (0, 1, 0, 1)  # Зеленый
                role_text = f'Твоя роль: {role} '
            elif role == 'Путана':
                self.role_label.color = (1, 0, 1, 1)  # Фиолетовый
                role_text = f'Твоя роль: {role} '
            elif role == 'Комиссар':
                self.role_label.color = (0, 0.5, 1, 1)  # Синий
                role_text = f'Твоя роль: {role} '
            else:  # Мирный
                self.role_label.color = (1, 1, 1, 1)  # Белый
                role_text = f'Твоя роль: {role} '
            
            self.role_label.text = role_text
            
            # Прячем кнопку показа и показываем кнопку "Далее"
            self.show_button.opacity = 0
            self.show_button.disabled = True
            self.next_button.opacity = 1
            self.next_button.disabled = False

    def next_player(self):
        """Переход к следующему игроку"""
        self.current_player_index += 1
        
        if self.current_player_index < len(self.roles):
            # Следующий игрок
            self.role_label.text = 'Нажмите кнопку'
            self.role_label.color = (1, 1, 0, 1)
            self.show_button.opacity = 1
            self.show_button.disabled = False
            self.next_button.opacity = 0
            self.next_button.disabled = True
            self.update_player_label()
        else:
            # Все игроки получили роли
            self.role_label.text = ' Все роли розданы! '
            self.role_label.color = (0, 1, 0, 1)
            self.player_label.text = 'Игра окончена'
            self.show_button.opacity = 0
            self.show_button.disabled = True
            self.next_button.opacity = 0
            self.next_button.disabled = True
            
            # Добавляем кнопку для возврата в главное меню (опционально)
            restart_button = Button(text='Вернуться в главное меню', font_size='18sp', size_hint=(1, 0.15))
            restart_button.on_press = self.restart_game
            self.add_widget(restart_button)
    
    def restart_game(self):
        """Перезапуск игры (возврат к первому экрану)"""
        self.manager.current = 'scr1'
        # Удаляем кнопку перезапуска
        for child in self.children:
            if hasattr(child, 'text') and child.text == 'Вернуться в главное меню':
                self.remove_widget(child)
                break