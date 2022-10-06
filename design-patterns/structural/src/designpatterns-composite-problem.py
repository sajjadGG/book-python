from dataclasses import dataclass, field


class Shape:
    def render(self) -> None:
        print('Render Shape')


@dataclass
class Group:
    __objects: list[Shape|'Group'] = field(default_factory=list)

    def add(self, obj: Shape|'Group') -> None:
        self.__objects.append(obj)

    def render(self) -> None:
        for obj in self.__objects:
            obj.render()


if __name__ == '__main__':
    group1 = Group()
    group1.add(Shape())  # square
    group1.add(Shape())  # square

    group2 = Group()
    group2.add(Shape())  # circle
    group2.add(Shape())  # circle

    group = Group()
    group.add(group1)
    group.add(group2)
    group.render()
