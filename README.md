# Inspiration Board: Back-end Layer

# Coworking Agreement

## Accessibility Needs
- Communicating needs on remote or in-person work
- Make sure everyone is on the same page/onboard

## Collaboration vs. individual work expectations
- Lean toward over-communicating, especially given remote work
- Keep people posted on what you're working on, esp if it's outside coworking time
- Maximize our work time during coworking

## Learning Style
- Sam: I am a little slow, so will often go back and review on my own! Don't mind me! Laura says + 1
- Sage: Visual learner, will likely need to review Learn lessons + past projects for refreshing

## Preferred Feedback Style
- I'm very direct, I hope not too much.
- If you notice something, please bring it up sooner rather than later, all suggestions welcome! Better to change things early on, especially with subjective front-end decisions
- Add comments to your code (if necessary)

## One Team Communication Skill to Improve
- Daily meetings and check-ins
- Deciding on a cutoff time/when teammates aren't expected to work on the project

## Signatures
Laura P., Sage C., Samantha H., and Thea V. (6/26/2023)

This scaffold includes the following:

## `app/__init__.py`

This file configures the app. It's where:

We expect developers to modify this file by:

- Replacing the database connection string
- Importing all models
- Registering all blueprints

Note that `create_app` also uses CORS. There is no extra action needed to be done with CORS.

## `app/routes.py`

We expect endpoints to be defined here.

The file already imports:

- `Blueprint`
- `request`
- `jsonify`
- `make_response`
- `db`

Feel free to alter these import statements.

This file also has a comment to define a Blueprint. Feel free to delete it.

## `app/models` Directory

This project already includes `app/models/board.py` and `app/models/card.py`, to anticipate the models `Board` and `Card`.

Both files already import `db`, for convenience!

## `requirements.txt`

This file lists the dependencies we anticipate are needed for the project.

## `Procfile`

This file already has the contents needed for a Heroku deployment.

If the `create_app` function in `app/__init__.py` is renamed or moved, the contents of this file need to change. Otherwise, we don't anticipate this file to change.
