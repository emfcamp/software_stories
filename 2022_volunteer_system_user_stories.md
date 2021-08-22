# Volunteer system

## User types

* Volunteer - People on the ground helping
* Volunteer Admin - Create shifts/roles etc.

> Might bring back Role Admin user type if we find any uses for it.  


## Availability

Allow volunteers to indicate that they are happy to be contacted (possibly restricted to certain times) to cover shifts where we are short of people.

As a volunteer I would like to:
-------------------------------
* Sign up to be a volunteer
  Providing:
      - email address
      - over 18 or not
  Optionally providing:
      - other contact details
  Pick which roles I'm interested in doing 
  Indicate availability to be contacted to cover shifts
    - Never
    - At any time during event
    - In specified time windows
* View all roles
    - Change which I'm interested in doing 
* View all shifts and filter by:
    - Role
    - Location
    - Shifts I can do (I have the training and pass the requirements)
    - Time
    - That I have signed up to
* Sign up for:
    - A specific shift 
* View list of shifts I'm signed up for
* Cancel a shift
* Take online training/test
    > Currently expect this to be only for the bar
* When on shift
    - Have access to information about the role (wiki page)
    - Update information about the role (edit wiki page)

As a Volunteer Admin I would like to:
----------------------------

*Before the event:*
* Create roles with
    - Name
    - Short description
    - wiki page with more details/instructions
    - Any requirements 
        - Must be over 18
        - Requires training
    - If they'll be "supervised" during shift or not
* Create venues with
    - A name
    - A location
    - Any other notes
* Create/Delete/Edit shifts
    - By:
        + Importing details (e.g. from frab, json)
        + Defining parameters
            * Time of the first shift
            * Shift duration
            * Number of shifts
            * Whether to repeat for all 3 days (e.g. bar will have different opening hours based on day)
        + Individually
    - With:
        + A role (e.g. 'A/V')
        + A venue (e.g. 'Stage A')
        + Start time
        + A hand-over period (a shift should probably start 15min before the previous shift is supposed to end to allow proper handover of information and so we have time to find replacements for no-shows)
        + A description box (to include links on 'how-to' as well as useful numbers etc.)
* Have the opportunity to preview any changes made to shifts before confirming them.

*During the event:*
* Sign a volunteer up for a shift
* Remove a volunteer from being signed up for a shift
* Edit shift info
* Ban a volunteer (and record a reason) from signing up for shifts
* View all volunteers that have signed up for a shift
* Contact:
    - All volunteers
    - All volunteers with certain training
    - All volunteers who have indicated that they may be contacted for cover now 
    - Volunteers signed up to particular shift(s)
* View which volunteers are currently in which shifts
* View which current shifts require volunteers
* View which upcoming shifts require volunteers
* View which current shifts are "unsupervised"

As someone being helped by volunteers I would like to:
-------------------------

*Before the event:*
* Provide volunteer manager(s) with details of 
    - Role(s)
    - Venue(s)
    - Shifts
    - Recurring runner tasks
    
*During the event:*
* Have volunteers turn up for the specified shifts
* Give those volunteers food tokens when they complete a shift
  > If there isn't going to be someone "supervising" volunteers: let volunteer admin know and we can check in on them and give them food tokens. 
* Get help from runners for ad-hoc tasks

Runner task system
-------------------------

We are going to have a pool of runners to cover smaller tasks don't need someone dedicated to them for the couple of hours of a normal shift. 

*Entering tasks (done by Volunteer Admin):*
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

*Performing tasks (done by runners):*
* View list of tasks to do ordered by time
* Mark a task as in progress
* Mark a task as done

> Can manage this on paper if we don't have time to make web version

It would be nice to have:
-------------------------
* Schedule integration
* Alerts
    - Option for volunteer to get reminder of shift they're signed up for N minutes before it starts
    - Via email, SMS, IRC, push notifications from website
* Admin Alerts (to IRC or a webpage we can watch) for:
    - Volunteer removing signup for a shift withing 15(?) minutes of the shift starting
    - Changes to role instruction wiki pages
    - If runner task is still TODO N minutes after scheduled time
* APIs for:
    - Individual's alerts
    - General alerts
    - The data set
