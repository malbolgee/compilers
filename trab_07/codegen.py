import re


class GenAssemblyMIPS:

    def __init__(self, intermediate, out) -> None:
        self.__intermediate_code_file = intermediate
        self.__out_file = out
        self.__tmp_reg = 0
        self.__register_number = 1
        self.__registers_table = {}
        self.__current_label = -1

        self.__EXPR = re.compile(r"(\w+) = (\w+|\d+) ([><*+-]|&&|\|\||>=|<=) (\w+|\d+)")
        self.__IF = re.compile(r"^if (\w+) goto (\w+), goto (\w+)$")
        self.__LABEL = re.compile(r"^L(\d+):$")
        self.__ASSIGNMENT = re.compile(r"^(\w+) = (\w+)$")
        self.__GOTO = re.compile(r"^goto (\w+)$")

        self.__find_next_label()

    def generate(self):
        self.__write_code_section()
        self.__read_file()

    def __new_label(self):
        self.__current_label += 1
        return f"L{self.__current_label}"

    def __find_next_label(self):
        with open(self.__intermediate_code_file, encoding="utf-8") as input:

            bigger = -1
            for line in input.readlines():

                expr_match = self.__LABEL.match(line)

                if expr_match:
                    number = expr_match.groups()[0]
                    number = int(number)
                    if int(number) > bigger:
                        bigger = number

        self.__current_label = bigger

    def __write_data_section(self):
        print(f"    .data", file=self.__out_file)
        print(f"    .word")

    def __write_code_section(self):
        print(f"    .code", file=self.__out_file)

    def __read_file(self):
        with open(self.__intermediate_code_file) as input:

            for line in input.readlines():
                expr_match = self.__EXPR.match(line)
                if_match = self.__IF.match(line)
                label_match = self.__LABEL.match(line)
                assng_match = self.__ASSIGNMENT.match(line)
                goto_match = self.__GOTO.match(line)

                if assng_match:
                    rd, ra = assng_match.groups()

                    is_imediate = ra.isnumeric()
                    rd = self.__get_register(rd)
                    if not is_imediate:
                        ra = self.__get_register(ra)

                    suffix, hashtag = ("i", "#") if is_imediate else ("", "")

                    print(
                        f"    add{suffix} {rd}, r0, {hashtag}{ra}", file=self.__out_file
                    )

                if label_match:
                    print(f"L{label_match.groups()[0]}:", file=self.__out_file)

                if if_match:
                    rd, if_label, else_label = if_match.groups()
                    rd = self.__get_register(rd)
                    print(f"    bnez {rd}, {if_label}", file=self.__out_file)
                    print(f"    b {else_label}", file=self.__out_file)

                if goto_match:
                    print(f"    j {goto_match.groups()[0]}", file=self.__out_file)

                if expr_match:
                    rd, rs, op, ra = expr_match.groups()

                    rd = self.__get_register(rd)
                    rs = self.__get_register(rs)

                    is_imediate = ra.isnumeric()

                    if not is_imediate:
                        ra = self.__get_register(ra)

                    suffix, hashtag = ("i", "#") if is_imediate else ("", "")

                    if op == "+":
                        print(
                            f"    add{suffix} {rd}, {rs}, {hashtag}{ra}",
                            file=self.__out_file,
                        )

                    elif op == "-":
                        print(
                            f"    sub{suffix} {rd}, {rs}, {hashtag}{ra}",
                            file=self.__out_file,
                        )

                    elif op == "*":
                        if is_imediate:
                            self.__tmp_reg = self.__register_number + 1
                            print(
                                f"    addi r{self.__tmp_reg}, r0, {ra}",
                                file=self.__out_file,
                            )
                            print(
                                f"    mult r{rs}, {self.__tmp_reg}",
                                file=self.__out_file,
                            )
                        else:
                            print(f"    mult {rs}, {ra}", file=self.__out_file)

                        print(f"    mflo {rd}", file=self.__out_file)

                    elif op == "/":
                        if is_imediate:
                            self.__tmp_reg = self.__register_number + 1
                            print(
                                f"    addi r{self.__tmp_reg}, r0, {ra}",
                                file=self.__out_file,
                            )
                            print(
                                f"    div r{rs}, {self.__tmp_reg}",
                                file=self.__out_file,
                            )
                        else:
                            print(f"    div {rs}, {ra}", file=self.__out_file)

                        print(f"    mflo {rd}", file=self.__out_file)

                    elif op == "%":
                        if is_imediate:
                            self.__tmp_reg = self.__register_number + 1
                            print(
                                f"    addi r{self.__tmp_reg}, r0, {ra}",
                                file=self.__out_file,
                            )
                            print(
                                f"    div r{rs}, {self.__tmp_reg}",
                                file=self.__out_file,
                            )
                        else:
                            print(f"    div {rs}, {ra}", file=self.__out_file)

                        print(f"    mfhi {rd}", file=self.__out_file)

                    elif op == "<":
                        print(
                            f"    slt{suffix} {rd}, {rs}, {hashtag}{ra}",
                            file=self.__out_file,
                        )

                    elif op == ">":
                        if is_imediate:
                            print(f"    slti {rd}, {rs}, #-{ra}", file=self.__out_file)
                        else:
                            print(f"    slt {rd}, {ra}, {rs}", file=self.__out_file)

                    elif op == "==" or op == "!=":
                        if is_imediate:
                            print(f"    xori {rd}, {rs}, #{ra}", file=self.__out_file)
                        else:
                            print(f"    xor {rd}, {rs}, {ra}", file=self.__out_file)

                    elif op == "<=":
                        # TODO: add immediate operation
                        print(f"    slt {rd}, {ra}, {rs}", file=self.__out_file)
                        print(f"    xori {rd}, {rd}, #1", file=self.__out_file)

                    elif op == ">=":
                        # TODO: add immediate operation
                        tmp_reg = self.__register_number + 1
                        print(f"    addi r{tmp_reg}, {rs}, #1", file=self.__out_file)
                        print(f"    slt {rd}, {ra}, r{tmp_reg}", file=self.__out_file)

                    elif op == "&&":
                        print(f"    and {rd}, {rs}, {ra}", file=self.__out_file)

                    elif op == "||":
                        print(f"    or {rd}, {rs}, {ra}", file=self.__out_file)

    def __get_register(self, var: str) -> str:
        reg = self.__registers_table.get(var)

        if not reg:
            self.__register_number += 1
            self.__registers_table[var] = self.__register_number
            return f"r{self.__register_number}"

        return f"r{reg}"

    def __add(self):
        pass
