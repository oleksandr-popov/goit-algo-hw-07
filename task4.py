class Comment:
    """
    Представляє один коментар у системі.
    """
    def __init__(self, text: str, author: str, comment_id: int):
        self.comment_id = comment_id
        self.text = text
        self.author = author
        # Список, що містить об'єкти Comment, які є відповідями
        self.replies: list['Comment'] = []
        
    def add_reply(self, reply: 'Comment'):
        """Додає дочірній коментар (відповідь) до поточного."""
        self.replies.append(reply)
        
    def __repr__(self) -> str:
        """Представлення об'єкта для налагодження."""
        return f"Comment(id={self.comment_id}, author='{self.author}', text='{self.text[:30]}...')"

class CommentSystem:
    """
    Керує ієрархічною структурою коментарів.
    """
    def __init__(self):
        # Словник для швидкого доступу до коментарів за їх ID
        self.comments: dict[int, Comment] = {}
        # Список коментарів верхнього рівня (без батьків)
        self.top_level_comments: list[Comment] = []
        # Лічильник для унікальних ID
        self._next_id = 1
        
    def _generate_id(self) -> int:
        """Генерує унікальний ID для нового коментаря."""
        new_id = self._next_id
        self._next_id += 1
        return new_id
        
    def add_comment(self, text: str, author: str, parent_id: int = None) -> Comment:
        """
        Додає новий коментар.
        
        :param text: Текст коментаря.
        :param author: Автор коментаря.
        :param parent_id: ID коментаря, на який йде відповідь (опціонально).
        :return: Створений об'єкт Comment.
        """
        new_id = self._generate_id()
        new_comment = Comment(text, author, new_id)
        self.comments[new_id] = new_comment
        
        if parent_id is None:
            # Це коментар верхнього рівня
            self.top_level_comments.append(new_comment)
        else:
            # Це відповідь на існуючий коментар
            parent_comment = self.comments.get(parent_id)
            if parent_comment:
                parent_comment.add_reply(new_comment)
            else:
                # Якщо батьківський коментар не знайдено, додаємо його як верхній рівень
                print(f"Помилка: Батьківський коментар з ID {parent_id} не знайдено. Коментар додано до верхнього рівня.")
                self.top_level_comments.append(new_comment)
                
        return new_comment
        
    def _display_comment(self, comment: Comment, depth: int = 0):
        """Рекурсивна функція для виведення коментаря та всіх його відповідей."""
        indent = "  |->" * depth 
        print(f"{indent} [ID: {comment.comment_id}] ({comment.author}): {comment.text}")
        
        # Рекурсивно викликаємо для кожної відповіді
        for reply in comment.replies:
            self._display_comment(reply, depth + 1)
            
    def display_all(self):
        """Виводить усі коментарі в ієрархічному порядку."""
        print("\n--- Коментарі ---")
        if not self.top_level_comments:
            print("Коментарі відсутні.")
            return

        for comment in self.top_level_comments:
            self._display_comment(comment)
        print("----------------------------\n")


# Test example

if __name__ == "__main__":
    cs = CommentSystem()
    
    c1 = cs.add_comment("Перший коментар", "Аліса")
    c2 = cs.add_comment("І що з того, що ти перший? Де логіка?", "Денис", parent_id=c1.comment_id)
    c3 = cs.add_comment("А яка загалом тема цього чата?", "Владимир")
    c4 = cs.add_comment("Вона війша з чата (((( ", "Діана", parent_id=c2.comment_id)
    c5 = cs.add_comment("А чи не бажаэте анекдот про такі розмови? ", "Єва", parent_id=c1.comment_id)
    
    cs.display_all()