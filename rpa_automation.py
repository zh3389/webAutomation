import PySimpleGUI as sg
import rpa as r
import time
import random


class OpenUrl:
    """刷网页"""
    def __init__(self, vis_chrome=False) -> None:
        self.r = r
        self.r.init(visual_automation=True, headless_mode=vis_chrome)

    def wait_sec(self, url_list, time_interval=[1, 3]):
        print(time_interval)
        for url in url_list:
            self.r.url(url)
            self.r.wait(delay_in_seconds=random.randint(time_interval[0], time_interval[1]))

    def close_window(self):
        self.r.close()

class OverdueJudgment:
    """软件过期判断"""
    def __init__(self) -> None:
        pass

    def now_time(self):
        print(time.time())
        return time.time()

    def expiration_time(self):
        return time.time() + 86400  # +86400为1天后过期

    def judge_expired(self):
        nowtime = self.now_time()
        aftertime = self.expiration_time()
        if nowtime > aftertime:
            return True
        else:
            return False

class OpenUrlGui:
    def __init__(self) -> None:
        # Define the window's contents
        self.layoutl = [[sg.Text("请输入你需要自动访问的网址,一行一个...")],
                        [sg.Multiline('www.baidu.com', size=(40,20), key='-INPUT-')],
                        ]
        self.layoutr = [[sg.Text("以防频率太高被检测, 执行完一遍暂停时间, 建议60秒左右.)")],
                        [sg.Input("60", key='-SEC-', size=(22))],
                        [sg.Text("页面停留时间 (提高访问的有效性, 建议5~10秒)")],
                        [sg.Input("5", key='-SECA-', size=(10)), sg.Input("10", key='-SECB-', size=(10))],
                        [sg.Text("请输入访问所有网址为一次的次数...")],
                        [sg.Input("3", key='-NUM-', size=(22))],
                        [sg.Text("是否后台刷访问.")],
                        [sg.Checkbox('True', key='-BOOL-')],
                        [sg.Button('Ok'), sg.Button('Quit')]
                        ]

        self.layout = [[sg.Col(self.layoutl), sg.Col(self.layoutr)]]

    def run(self):
        # Create the window
        self.window = sg.Window('刷访问量', self.layout)
        while True:
            self.event, self.values = self.window.read()
            time_inter = [int(self.values['-SECA-']), int(self.values['-SECB-'])]
            if self.event == "Ok":
                url_list = []
                for url in self.values['-INPUT-'].split("\n"):
                    url_list.append(url)
                for _ in range(int(self.values['-NUM-'])):
                    ou = OpenUrl(vis_chrome=self.values['-BOOL-'])  # 创建刷访问量的对象
                    sg.one_line_progress_meter('进度条', _+1, int(self.values["-NUM-"]), '任务完成进度', orientation='h')
                    ou.wait_sec(url_list, time_interval=time_inter)
                    ou.close_window()
                    time.sleep(int(self.values['-SEC-']))
                sg.popup_ok('已刷完')
            if self.event == sg.WINDOW_CLOSED or self.event == 'Quit':
                break
        # Finish up by removing from the screen
        self.window.close()

if __name__ == '__main__':
    oj = OverdueJudgment()
    if oj.judge_expired():
        pass
    else:
        oug = OpenUrlGui()
        oug.run()
