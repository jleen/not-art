import dryck
import shutil

class GptContext(dryck.HtmlContext):
    replace = {'§': '◊sep'}

    def sep(self):
        return '<p class="sep">✼</p>'

dryck.render(GptContext(), 'gpt.dryck', 'index.html.dryck', 'dist/index.html')
shutil.copy('style.css', 'dist/style.css')
