import os

# Telegram Bot Configuration
API_ID = int(os.getenv('API_ID', '23781502'))
API_HASH = os.getenv('API_HASH', '53fd41bf872ff90db953e48240c1b58c')
BOT_TOKEN = os.getenv('BOT_TOKEN', '7409375565:AAHqOX7eqXy0yuoNhkYVqGkmud6ON1PYndU')
BOT_NAME = os.getenv('BOT_NAME', 'chattttt')
BOT_USERNAME = os.getenv('BOT_USERNAME', 'uhidfgrgrebot')
OWNER_ID = int(os.getenv('OWNER_ID', '7160721143'))
OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'iam_dhruv_dubey')
UPDATE_CHANNEL = os.getenv('UPDATE_CHANNEL', 'Devine_Community')
SUPPORT_GROUP = os.getenv('SUPPORT_GROUP', 'Devine_Community')

# OpenAI Configuration
OPENAI_KEY = os.getenv('OPENAI_KEY', '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')

# MongoDB Configuration
MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority')

# Check if all required environment variables are set
if not all([API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, OWNER_ID, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP, MONGODB_URL]):
    raise RuntimeError("Please set all required environment variables: API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, OWNER_ID, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP, MONGODB_URL")
