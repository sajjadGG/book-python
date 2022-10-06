class Button:
    __label: str

    def set_label(self, name):
        self.__label = name

    def get_label(self):
        return self.__label

    def click(self):
        ...


if __name__ == '__main__':
    button = Button()
    button.set_label('My Button')
    button.click()
