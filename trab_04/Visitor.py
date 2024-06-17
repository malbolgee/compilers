from HtmlParser import HtmlParser
from HtmlVisitor import HtmlVisitor


class Visitor(HtmlVisitor):
    def __init__(self):
        self.output = ""
        self.question_counter = 0

    def visitRoot(self, ctx: HtmlParser.RootContext):
        for child in ctx.questao():
            self.visit(child)
        return self.output

    def visitQTexto(self, ctx: HtmlParser.QTextoContext):
        cols = ctx.NUMERO(0).getText()
        rows = ctx.NUMERO(1).getText()
        question_text = ctx.str_().getText().strip('"')
        self.output += f"{question_text}<br>\n"
        self.output += f"<textarea name='Q{self.question_counter}' cols='{cols}' rows='{rows}'></textarea><br>\n<br>\n"
        self.question_counter += 1

    def visitQRadioBox(self, ctx: HtmlParser.QRadioBoxContext):
        question_text = ctx.str_().getText().strip('"')
        self.output += f"{question_text}<br>\n"
        for option in ctx.opcoes().str_():
            option_text = option.getText().strip('"')
            self.output += f"<input type='radio' name='Q{self.question_counter}' value='{option_text}'>{option_text}<br>\n"
        self.output += "<br>\n"
        self.question_counter += 1

    def visitQCheckBox(self, ctx: HtmlParser.QCheckBoxContext):
        question_text = ctx.str_().getText().strip('"')
        self.output += f"{question_text}<br>\n"
        for option in ctx.opcoes().str_():
            option_text = option.getText().strip('"')
            self.output += f"<input type='checkbox' name='Q{self.question_counter}' value='{option_text}'>{option_text}<br>\n"
            self.question_counter += 1
        self.output += "<br>\n"

    def visitQMenu(self, ctx: HtmlParser.QMenuContext):
        menu_id = ctx.IDENT().getText()
        menu_label = ctx.str_().getText().strip('"')
        self.output += f"<label for='{menu_id}'>{menu_label}</label><br>\n"
        self.output += f"<select name='{menu_id}' id='{menu_id}'>\n"
        for option in ctx.opcoesMenu().menuOpcao():
            option_id = option.IDENT().getText()
            option_label = option.str_().getText().strip('"')
            self.output += f"  <option value='{option_id}'>{option_label}</option>\n"
        self.output += "</select><br>\n<br>\n"

    def visitQBotao(self, ctx: HtmlParser.QBotaoContext):
        button_label = ctx.str_(0).getText().strip('"')
        alert_message = ctx.str_(1).getText().strip('"')
        self.output += f"<button type='button' onclick=\"alert('{alert_message}')\">{button_label}</button><br>\n<br>\n"
