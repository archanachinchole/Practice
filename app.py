from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        print(request.form)  # Print the form data received
        values = [
            {
                'index': request.form[f'values_index{i}_index'],
                'year': request.form[f'values_index{i}_year'],
                'Number_of_new_courses_intro': request.form[f'values_index{i}_Number_of_new_courses_intro'],
                'Number_of_Courses_offered': request.form[f'values_index{i}_Number_of_Courses_offered'],
            } for i in range(1, 6)
        ]

        # Your processing logic here

        sum_1_2_1_1 = sum(int(data['Number_of_new_courses_intro']) for data in values)
        sum_1_2_1_2 = sum(int(data['Number_of_Courses_offered']) for data in values)
        result_1_2 = round((sum_1_2_1_1 / sum_1_2_1_2) * 100, 2)

        return render_template('result.html', values=values, result_1_2=result_1_2)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
