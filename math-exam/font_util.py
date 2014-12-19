# -*- coding: utf-8 -*-

# A hack from http://markmail.org/message/oxsn7avgxfjvonof
def useChineseFont():
    import reportlab.rl_config
    reportlab.rl_config.warnOnMissingFontGlyphs = 0
    import reportlab.pdfbase.pdfmetrics
    import reportlab.pdfbase.ttfonts
    reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('uming','./uming.ttc'))
    import reportlab.lib.fonts
    reportlab.lib.fonts.ps2tt = lambda psfn: ('kaiu', 0, 0)
    reportlab.lib.fonts.tt2ps = lambda fn,b,i: 'kaiu'
    # for CJK Wrap
    import reportlab.platypus
    def wrap(self, availWidth, availHeight):
        # work out widths array for breaking
        self.width = availWidth
        leftIndent = self.style.leftIndent
        first_line_width = availWidth - (leftIndent+self.style.firstLineIndent) - self.style.rightIndent
        later_widths = availWidth - leftIndent - self.style.rightIndent
        try:
            self.blPara = self.breakLinesCJK([first_line_width, later_widths])
        except:
            self.blPara = self.breakLines([first_line_width, later_widths])
        self.height = len(self.blPara.lines) * self.style.leading
        return (self.width, self.height)
    reportlab.platypus.Paragraph.wrap = wrap
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
