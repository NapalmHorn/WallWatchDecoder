#  wwd_gui.py
"""a gui interface for configuring the wall watcher decoder program I wrote
This will allow the user to chose rules that require certain values for
keys in the log files."""
        #TODO far future:
        # add chart functionality
        # create a chart with pg chart
        # set chart options


#Import needed classes
from wallwatcherdecoder import log_report, entry
import button
import graphics  # http://mcsp.wartburg.edu/zelle/python/graphics.py
import tkinter.filedialog


def main():
    # draw main window
    win = graphics.GraphWin("Decode and filter wallwatcher logs", 440, 200)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # choose the log file () to open
    select_logs_btn = button.Button(win, graphics.Point(7.5, 8), 5, 1,
        "Choose Log file[s] to decode")
    select_logs_btn.activate()

    # set the output file for csv file
    set_csv_out_btn = button.Button(win, graphics.Point(2.5, 8), 5, 1,
        "Set output file")
    set_csv_out_btn.activate()

    # choose the values to filter
    select_filters_btn = button.Button(win, graphics.Point(2.5, 6), 5,
        1, "Set Filters")
    select_filters_btn.activate()

    # run the decoder
    decode_now_btn = button.Button(win, graphics.Point(7.5, 6),
        5, 1, "Decode Now")

    # choose the sortkey
    change_sort_key_btn = button.Button(win, graphics.Point(2.5, 4),
        5, 1, "Sort by ...")
    change_sort_key_btn.activate()

    # quit button
    quit_btn = button.Button(win, graphics.Point(7.5, 4), 5, 1, "quit")
    quit_btn.activate()

    #Set defaults and create data structures
    log = log_report()
    outfile = 'ouput.csv'
    log_names = []
    lines = []

    #click loop
    pt = win.getMouse()
    while not quit_btn.clicked(pt):
        if select_logs_btn.clicked(pt):
            log_names = select_logs()
            if log_names:
                decode_now_btn.activate()
        elif decode_now_btn.clicked(pt):
            for filename in log_names:
                # create a list of lines from the file
                f = open(filename, 'r')
                lines += f.readlines()
                f.close()

                # create an entry for each and add entry
                for line in lines:
                    entry_line = entry(line)
                    log.add(entry_line)

            # sort and write the CSV file
            log.write_csv(outfile)
            decode_now_btn.deactivate()
        elif select_filters_btn.clicked(pt):
            values = select_filters()
            print(str(values))
            if values:
                log.setScope(values)
        elif set_csv_out_btn.clicked(pt):
            outfile = set_csv_out()
        elif change_sort_key_btn.clicked(pt):
            new_key = change_sort_key()
            if new_key:
                log.setSortKey(new_key)
        pt = win.getMouse()


def select_logs():
    return  tkinter.filedialog.askopenfilenames()


def select_filters():
    win_sf = graphics.GraphWin("Filter on return:", 300, 400)
    win_sf.setCoords(0.0, 0.0, 2.0, 12.0)
    button_count = 0
    button_list = []
    values = []
    entry_fields = {}
    good_keys = ['date', 'time', 'code', 'protocol', 'remote_ip',
            'remote_domain', 'remote_port', 'local_ip', 'local_port']

    for field in good_keys:
        button_list.append(button.Button(win_sf, graphics.Point(.5, 1 +
        button_count), 1, 1, field))
        button_count += 1
        button_list[-1].activate()
        entry_fields[field] = graphics.Entry(graphics.Point(1.505,
        button_count), 16)
        entry_fields[field].draw(win_sf)

    button_count += 1
    quit_sf_btn = button.Button(win_sf, graphics.Point(.5, 1 + button_count),
        1, 1, 'Save & quit')
    quit_sf_btn.activate()
    cancel_sf_btn = button.Button(win_sf, graphics.Point(1.5,
        1 + button_count), 1, 1, 'Abandon changes')
    cancel_sf_btn.activate()

    #click loop for getting filters
    pt = win_sf.getMouse()
    while not (quit_sf_btn.clicked(pt) or cancel_sf_btn.clicked(pt)):
        for btn in button_list:
            if btn.clicked(pt):
                field = btn.getLabel()
                values.append((field, entry_fields[field].getText()))
                btn.deactivate()
        pt = win_sf.getMouse()

    #close popup
    win_sf.close()
    if quit_sf_btn.clicked(pt):
        return values
    else:
        return []


def set_csv_out():
    return tkinter.filedialog.asksaveasfilename(filetypes=[
        ('csv', '*.csv'), ('allfiles', '*')])


def change_sort_key():
    win_sort = graphics.GraphWin("Filter on return:", 150, 400)
    win_sort.setCoords(0.0, 0.0, 1.0, 12.0)
    good_keys = ['date', 'time', 'code', 'protocol', 'remote_ip',
            'remote_domain', 'remote_port', 'local_ip', 'local_port']
    button_count = 0
    button_list = []

    #create a collomn of buttons
    for field in good_keys:
        button_list.append(button.Button(win_sort, graphics.Point(.5, 1 +
            button_count), 1, 1, field))
        button_count += 1
        button_list[-1].activate()

    quit_sort_btn = button.Button(win_sort, graphics.Point(.5, 1 +
        button_count), 1, 1, 'Quit')
    quit_sort_btn.activate()

    #get a click
    pt = win_sort.getMouse()
    while not quit_sort_btn.clicked(pt):
        for btn in button_list:
            if btn.clicked(pt):
                win_sort.close()
                return btn.getLabel()

    win_sort.close()
    return None

if __name__ == '__main__':
    main()