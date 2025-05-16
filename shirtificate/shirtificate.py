from fpdf import FPDF, Align

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", size=48)
        self.cell(80)
        self.cell(30, 60, "CS50 Shirtificate", border=1, align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    message = f"{name} took CS50"

    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.image("shirtificate.png", x=Align.C, y=80, w=175)

    pdf.set_y(150)
    pdf.cell(0, 10, message, align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
