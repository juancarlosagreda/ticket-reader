# ticket-reader

ticket-reader is a React-Flask-Firebase web application for the extraction of ticket data from images, all integrated into a React.js frontend app.

![Alt Text](./assets/walkthrough.gif)

## Installation

First, clone the repository into your device and ask for the API Keys.

```bash
git clone https://github.com/juancarlosagreda/ticket-reader.git
```

Start with installing the python dependencies, and add the config/key files into server folder.

```bash
cd ticket-reader/sever
pip install requirements.txt
```

Startup the backend application

```bash
python app.py
```

Now set up the frontend application. The pre-requisites are to have [node.js](https://nodejs.org/en/#home-downloadhead) and [yarn](https://classic.yarnpkg.com/en/docs/install/#mac-stable) installed. 

```bash
cd ..
cd client
yarn
```

Startup the frontend application

```bash
yarn start
```

## Usage

From the main page, click on new ticket and see the changes on the total value and on the database by clicking on the transactions page.

## Licence

- [Themesberg](https://github.com/themesberg/volt-react-dashboard)
- [MIT](https://themesberg.com/licensing#mit)
