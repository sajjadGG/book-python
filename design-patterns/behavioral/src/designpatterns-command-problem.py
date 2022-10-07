class Button:
    label: str

    def set_label(self, name):
        self.label = name

    def get_label(self):
        return self.label

    def click(self):
        ...


if __name__ == '__main__':
    button = Button()
    button.set_label('My Button')
    button.click()
