from Intern_proj  import create_app

app=create_app()

if __name__ == '__main__':
    app.run(debug=Flase,host='0.0.0.0')
