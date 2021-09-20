# Volunteer system

## User types

* Volunteer - People on the ground helping
* Volunteer Admin - Create shifts/roles etc.

> Might bring back Role Admin user type if we find any uses for it.  

* Unsupervised - Volunteer team are looking after this role rather than another team

## As a volunteer I would like to:

* Sign up to be a volunteer
    - Providing:
      - email address
      - over 18 or not
    - Optionally providing:
      - other contact details - key/value table for arbitrary contact types
    - Pick which roles I'm interested in doing  - new feature/improvement?
    - Indicate availability to be contacted to cover shifts
      - Never
      - At any time during event
      - In specified time windows - new feature

* View all roles
    - Change which I'm interested in doing 

* View all shifts and filter by (schedule view):
    - Role
    - Location
    - Shifts I can do (I have the training and pass the requirements)
    - Time
    - That I have signed up to

* Sign up for:
    - A specific shift 

* View list of shifts I'm signed up for - link to schedule view search
* Cancel a shift - improve
* Take online training/test
    > Currently expect this to be only for the bar

* When on shift
    - Have access to information about the role (wiki page)
    - Update information about the role (edit wiki page)

## As a Volunteer Admin I would like to:

### Before the event

* Create roles with
    - Name
    - Short description
    - wiki page with more details/instructions
    - Any requirements 
        - Must be over 18
        - Requires training
    - If they'll be "unsupervised" during shift or not

* Create venues with
    - A name
    - A location
    - Any other notes
      > Probably do want to add field for this in DB

* Create/Delete/Edit shifts
    - With:
        + A role (e.g. 'A/V')
        + A venue (e.g. 'Stage A')
        + Start time
        + End time
        + Minimum number needed
        + Maximum number needed
    - By:
        + Manually entering details
        + Importing details from 
            * Main schedule
              > For any shifts tied to something from the schedule
            * json file
              > Will let us have external tools to build lists of shifts
            * shift creation tool currently exists as a Python script with no web UI
        + Create multiple shifts by defining parameters
            * Time of the first shift
            * Shift duration
            * Number of shifts
            * Whether to repeat for all 3 days (e.g. bar will have different opening hours based on day)

* Have the opportunity to preview any created shifts or changes made to shifts before confirming them (especially for importing or creating from parameters). - new feature

### During the event

* Sign a volunteer up (add new volunteer record) - new feature
* Sign a volunteer up for a shift (either if they have already signed up to volunteer system
* Remove a volunteer from being signed up for a shift
* Edit shift info
* Ban a volunteer (and record a reason) from signing up for shifts
* View all volunteers that have signed up for a shift
* Contact:
    - All volunteers
    - All volunteers with certain training
    - All volunteers who have indicated that they may be contacted for cover now 
    - Volunteers signed up to particular shift(s)
* View which volunteers are currently in which shifts - schedule view
* View which current shifts require volunteers - schedule view
* View which upcoming shifts require volunteers - schedule view
* View which current shifts are "unsupervised" - schedule view

## As someone being helped by volunteers I would like to:

### Before the event
* Provide volunteer manager(s) with details of 
    - Role(s)
    - Venue(s)
    - Shifts
    - Recurring runner tasks
    
### During the event
* Have volunteers turn up for the specified shifts
* Give those volunteers food tokens when they complete a shift
  > If someone is "unsupervised": let volunteer admin know and we can check in on them and give them food tokens.
* Get help from runners for ad-hoc tasks

## Runner task system

We are going to have a pool of runners to cover smaller tasks don't need someone dedicated to them for the couple of hours of a normal shift. 

### Entering tasks 

Will be done by Volunteer Admin - for people wanting a task done: ping details to volunteer desk and they'll put it in the system to get someone to do it):

* Create recurring task with:
    - Name
    - Description
    - Schedule
        - Start/stop times
        - Frequency
    - Number of people needed
    - Who to contact for more info, if there are any problems etc.
* Create one off task - as for recurring task but single time rather than schedule.
* Cancel a task
    - For recurring tasks want to support cancelling one instance or all future instances
* Postpone a task 

### Performing tasks (done by runners)
* View list of tasks to do ordered by time
* Mark a task as in progress
* Mark a task as done

> Can manage this on paper if we don't have time to make web version

## It would be nice to have
* Schedule integration
* Alerts
    - Option for volunteer to get reminder of shift they're signed up for N minutes before it starts
    - Via email, IRC, push notifications from website
    - See other contact details (key/value table for arbitrary information)
* Admin Alerts (to IRC or a webpage we can watch) for:
    - Volunteer removing signup for a shift within 15(?) minutes of the shift starting
    - Changes to role instruction wiki pages (watches on pages in Mediawiki, ideally pass to an IRC bot)
    - If runner task is still TODO N minutes after scheduled time
* APIs for:
    - Individual's alerts
    - General alerts
    - The data set
* Dashboard - something to run at volunteer desk to auto update with current status.
