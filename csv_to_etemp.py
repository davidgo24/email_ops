import pandas as pd

def generate_email_template(row, template_path):
    """Generates an email template from a row of data and a template file."""

    with open(template_path, 'r') as f:
        template = f.read()

    email = row['Column 5']
    sales_order_number = row['Column 2']
    full_name = row['Column 3']

    template = template.format(
        email=email,
        sales_order_number=sales_order_number,
        full_name=full_name
    )

    return template

def process_excel_and_generate_txt(excel_file, template_path, output_txt):
    """Processes an Excel file, generates email templates, and saves them to a txt file."""

    df = pd.read_excel(excel_file)

    with open(output_txt, 'w') as f:
        for index, row in df.iterrows():
            if row['Column 11'] == 'NW' and 'DO NOT EMAIL' not in str(row['Column 8']).strip():
                email_template = generate_email_template(row, template_path)
                f.write(email_template)
                f.write('\n\n')  # Add two line breaks between emails

# Example usage
excel_file = 'test_data.xlsx'  # Replace with your Excel file path
template_path = 'nationwide_delivery.txt' # Replace with your template file path
output_txt = 'email_templates.txt' # Replace with your desired output txt file path

process_excel_and_generate_txt(excel_file, template_path, output_txt)