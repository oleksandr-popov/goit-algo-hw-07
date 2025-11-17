class Comment:
    """
    Представляє один коментар у ієрархічній системі.
    """
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        # Список, що містить об'єкти Comment, які є відповідями
        self.replies: list['Comment'] = []
        # Прапорець для відстеження стану видалення
        self.is_deleted = False
        
    def add_reply(self, reply: 'Comment'):
        """
        Додає дочірній коментар (відповідь) до поточного.
        """
        self.replies.append(reply)
        
    def remove_reply(self, deletion_message: str = "Цей коментар було видалено."):
        """
        Видаляє коментар, змінюючи його текст на стандартне повідомлення
        і встановлюючи прапорець is_deleted в True.
        """
        self.text = deletion_message
        self.author = "Видалено" # Змінюємо автора для ясності
        self.is_deleted = True
        # Відповіді залишаються, щоб не порушити ієрархію
        
    def display(self, depth: int = 0):
        """
        Рекурсивно виводить коментар та всі його відповіді, використовуючи відступи.
        
        :param depth: Поточний рівень вкладеності (використовується для відступу).
        """
        indent = "\t" * depth 
        
        if self.is_deleted:
            # Виведення видаленого коментаря
            print(f"{indent} [Видалено]: {self.text}")
        else:
            # Виведення активного коментаря
            print(f"{indent} {self.author}: {self.text}")
        
        # Рекурсивно викликаємо display для кожної відповіді, збільшуючи глибину
        for reply in self.replies:
            reply.display(depth + 1)

# Test example
# 1. Створення коментарів
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# 2. Додавання відповідей до кореневого коментаря
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# 3. Створення відповіді на відповідь (вкладення)
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# 4. Видалення коментаря (reply1).
# Зверніть увагу, що його дочірній коментар (reply1_1) залишається у дереві.
reply1.remove_reply() 

# 5. Виведення всієї ієрархії
root_comment.display()
