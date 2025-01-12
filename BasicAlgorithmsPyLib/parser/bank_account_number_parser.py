from typing import List, Optional


def parse_bank_account(bank_account: str) -> Optional[int]:
  """
  Парсит строку с номером банковского счета, которая выглядит следующим образом:
   _     _  _     _  _  _  _  _
  | |  | _| _||_||_ |_   ||_||_|
  |_|  ||_  _|  | _||_|  ||_| _|
  
  Пример строки на ввод (вернёт: 123456789):
  '    _  _     _  _  _  _  _ \n'+
  '  | _| _||_||_ |_   ||_||_|\n'+
  '  ||_  _|  | _||_|  ||_| _|\n'
  
  Args:
    bank_account: номер банковского счёта в формате специальной строки,
    составленной из пайпов и подчеркиваний.
  
  Returns:
    Номер банковского счета в формате int из указанной строки.
  """
  lines: List[str] = bank_account.split('\n', 2)
  
  if len(lines) != 3:
    return None
  
  digits: List[int] = []
  
  for i, _ in enumerate(lines[0]):
    if i % 3 == 0:
      digit: List[str] = [
        lines[0][i:i+3],
        lines[1][i:i+3],
        lines[2][i:i+3]
      ]
    else:
      continue
    
    match digit:
      case [' _ ', '| |', '|_|']:
        digits.append(0)
      case ['   ', '  |', '  |']:
        digits.append(1)
      case [' _ ', ' _|', '|_ ']:
        digits.append(2)
      case [' _ ', ' _|', ' _|']:
        digits.append(3)
      case ['   ', '|_|', '  |']:
        digits.append(4)
      case [' _ ', '|_ ', ' _|']:
        digits.append(5)
      case [' _ ', '|_ ', '|_|']:
        digits.append(6)
      case [' _ ', '  |', '  |']:
        digits.append(7)
      case [' _ ', '|_|', '|_|']:
        digits.append(8)
      case [' _ ', '|_|', ' _|']:
        digits.append(9)
      case _:
        return None

  return int("".join(map(str, digits)))