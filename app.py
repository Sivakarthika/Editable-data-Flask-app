from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Sample dynamic DataFrame with more columns
df = pd.DataFrame({
    'columnA': ['row1', 'row2', 'row3'],
    'columnB': ['edit1', 'edit2', 'edit3'],
    'columnC': ['val1', 'val2', 'val3'],
    'columnD': ['val4', 'val5', 'val6'],
    # ... add up to 30 columns as needed
})

@app.route('/', methods=['GET', 'POST'])
def index():
    global df
    if request.method == 'POST':
        # Update only columnB
        for i in range(len(df)):
            df.at[i, 'columnB'] = request.form.get(f'columnB_{i}', df.at[i, 'columnB'])
        
        # Print updated DataFrame to console
        print("Updated DataFrame:")
        print(df)

        return redirect('/')  # Redirect to avoid form resubmission on refresh

    return render_template('index.html', df=df)

if __name__ == '__main__':
    app.run(debug=True)
