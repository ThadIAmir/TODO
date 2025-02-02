# TodoList 🎯

Welcome to **TodoList**, a simple yet powerful task management web application built with Django! 🚀 This project allows users to register, log in, use crud functions for each task, and mark them as completed while storing data in a PostgreSQL database. The application is deployed and accessible online via Railway.

## Features ✨

- **User Registration & Login**: Secure user authentication to keep your tasks private.
- **Task Management**: Create, view, edit, and delete tasks effortlessly.
- **Task List View**: See all your tasks in one convenient list.
- **Logout**: Securely log out when you're done.
- **PostgreSQL Integration**: Tasks are stored in a PostgreSQL database for reliable, scalable data storage.

## Demo 💻

Check out the live demo of the TodoList app hosted on Railway:  
[Live Demo](https://web-production-d168.up.railway.app/)

## Installation & Setup 🛠️

To get started with **TodoList**, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ThadIAmir/TODO.git
    cd TODO
    ```

2. **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use: venv\Scripts\activate
    ```

3. **Install the dependencies** using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup the database**:
    - Make sure you have PostgreSQL running locally or use the Railway-hosted version.
    - Create a `.env` file to store your database credentials. Example:
      ```plaintext
      DATABASE_URL=postgres://username:password@host:port/dbname
      ```

5. **Apply migrations** to set up your database:
    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

Your app should now be accessible at `http://127.0.0.1:8000/`.

✅Once the app is running, you can <b>Register a new account</b> to start managing your tasks.
<br><br>

## Technologies Used 🛠️

- **Django**: The web framework for building the backend.
- **PostgreSQL**: A robust relational database for storing tasks.
- **HTML/CSS**: For the frontend.
- **Bootstrap**: For responsive and modern design.
- **Railway.com**: For cloud deployment.

## Deployment 🌐

This project is deployed on [Railway](https://railway.app/), allowing you to easily access it online. If you'd like to deploy it yourself, Railway offers a simple deployment process that you can follow.

## Contributing 🤝

We welcome contributions to improve the project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Please ensure that your code follows the PEP 8 style guide and is well-documented.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions, suggestions, or issues! Happy coding! 💻
