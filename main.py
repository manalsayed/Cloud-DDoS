from pcpi import session_loader

# Load Prisma Cloud credentials
session_manager = session_loader.load_from_file()
cspm_session = session_manager.create_cspm_session()

# Get a list of cloud accounts
accounts = cspm_session.get('/cloud/accounts')

# Get compliance violations for an account
violations = cspm_session.get(f'/compliance/{account_id}/violations')

# ... and more
