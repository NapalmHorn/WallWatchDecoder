#  pygchart.py

"""
NapalmHorn Code

pgChart is an ultralightweight easy to use solution to creating charts in
python it use Google's Chart API Thus it creates good looking reasonable charts
in a fast and easy way.  basiclly I wanted a fast easy lightweight(no big
packages, dependences of complex api's) way to Take a log file count some stuff
and make a chart.
"""

import string


class gchart():

    def __init__(self, raw_data):
        self.html_data_tab = ''  # creats a blank chart to start this.
        self.import_raw_data(raw_data)
        self.chart_type = self.set_chart_type()

    def import_raw_data(self, chart_data):
        """ Inputs the chart_data from pgChart and creates a html table for use
        in the HTML file
        ok for use with multiple data points per label
        input defined as a dictionary of lists
        """
        self.html_data_tab += "['tag', 'data']"
        for data in chart_data.keys():
            # add a label and data row to the self.html_data_tab

            if self.html_data_tab:
                self.html_data_tab += ','
                #  if the chart is not blank put a comma at the end,
                #  saves unneeded trailing comma

            if str(data).find("'") + 1:
                #  fix raw ' in labels find returns -1
                #  if not found so +1 evals to zero => False
                self.html_data_tab += "\n          ['" + '---' + "'"
                #  add data one at a time to the line
            elif set(str(data)).isdisjoint(string.ascii_letters +
                    string.digits):
                self.html_data_tab += "\n          ['" + '---' + "'"
            else:
                self.html_data_tab += "\n          ['" + str(data) + "'"
                #  for each data entry create a new line.

            for datum in chart_data[data]:
                self.html_data_tab += ",   " + str(datum) + " "
                # add data one at a time to the line
            self.html_data_tab += '  ]'  # close the line
        self.html_data_tab += '\n        ]);\n'    # close chart
        return self.html_data_tab

    def set_chart_type(self):
        """should written in child class to set the chart type and fix the
        html files as needed"""
        return 'PieChart'

    def set_chart_options(self, options):
        """Sets various options for the chart"""
        None

    def html_options(self):
        """Returns a string such that the option are implemented as desired"""
        return ''

    def create_html(self):
        """Creats a string that is an html file """
        html = '<html>'
        f = open('prechart.not_quitehtml', 'r')
        html += f.read()
        f.close()

        html += self.html_data_tab
        html += self.html_options()

        f = open('postchart.not_quitehtml', 'r')
        # fix chart type here
        html += f.read().replace('PieChart', self.chart_type)
        f.close()
        html += '</html>'

        return html


class pie_chart(gchart):

    def set_chart_type(self):
        """should written in child class to set the chart type and fix the
        html files as needed"""
        return 'PieChart'
