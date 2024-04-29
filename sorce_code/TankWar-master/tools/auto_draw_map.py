
def func():
    import os
    import PySimpleGUI as sg

    path = r"D:\Coding Files\Workplace\PythonWorkplace\TankWar2.0\resources\images\walls"

    files = [path + "\\" + file for file in os.listdir(path)]

    sg.Image()

    layout = [
        [sg.Image(files[0], size=(30, 30), enable_events=True) for i in range(19)] for j in range(15)
    ]
    layout.append([sg.Button("Lưu bản đồ"), sg.Button("Đặt lại"), sg.Button("Thoát")])

    window = sg.Window("Vẽ bản đồ", layout)
    while True:
        event, values = window.read()
        if event in (None, "Xác nhận"):
            window.refresh()
        elif event in range(285):
            print(event)
            elem = window.find_element(event)
            num = elem.Filename.split("\\")[-1].split(".")[0]
            num = (int(num) + 1) % 5
            elem.Filename = files[num]
            elem.Update(files[num], size=(30, 30))
            window.refresh()
        elif event in (None, "Lưu bản đồ"):
            lines = []
            line = []
            img = 0
            for i in range(0, 15):
                for j in range(0, 19):
                    elem = window.find_element(img)
                    num = elem.Filename.split("\\")[-1].split(".")[0]
                    line.append(num)
                    img += 1
                lines.append(line)
                line = []

            content = "["
            for line in lines:
                content += "["
                for num in line:
                    content += num + ", "
                content += "],\n"
            content += "]"

            with open("map.txt", "w") as f:
                f.write(content)
        elif event == "Thoát":
            window.close()
            exit()

if __name__ == '__main__':
    func()