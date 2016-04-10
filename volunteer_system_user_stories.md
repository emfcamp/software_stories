# Volunteer system

## Roles
* Volunteer - People on the ground helping
* Manager - Check volunteers arrive for shifts, carry out training
* Admin - Create shifts/roles etc.

## Shift types
**NB:** not the same as roles. Roles are e.g. "bar", "A/V". Types are e.g. "training", "free"

* Training - Special shift that the volunteer must complete before being allowed to do other shifts of that type (e.g. bar training)
* Free shift - The volunteer indicates that they are happy to be assigned any shift they are trained to do for that period
* Cover - (not really a shift) the volunteer indicates that they are happy to be contacted to fill required shifts (not the same as free as cover could be at any time during the weekend).

As a volunteer I would like to:
-------------------------------
* View all roles
* View all shifts and filter by:
    - Role
    - Location
    - Shifts I can do (I have the training and pass the requirements)
    - Time
    - That I have signed up to
    - That don't clash with items in the schedule I've starred
* Sign up for:
    - A specific shift I have been trained for
    - A shift I have not been trained for:
        + ONLY if I can receive training before the shift starts ()
        +  
    - A free shift: any shift I am able to (i.e. be assigned a shift as needed)
    - A training session
* Sign up to be trained for a role
* Be notified
    - By:
        + Email
        + SMS
        + Push notification (from web app or native app)
    - About:
        + My upcoming shifts
        + Changes to my shift
        + Shifts that need covering
        + The type of shift I have been assigned (if I signed up as 'free')
* Be able to change my notification settings
* Be able to communicate with managers and/or an admin
* Provide extra information
    - Phone number
    - Age
    - Misc details (e.g. experience)
* When on shift
    - Log that my replacement has not arrived on time (if unmanaged)
    - Request help at any time
    - Have access to information about the role
* Change a shift
    - And be alerted if doing so will flag me as a no-show for that shift (i.e. if I try to change a shift within 15 min of its start)


As a manager I would like to:
-----------------------------
* Assign free volunteers to shifts
* Change who's on a shift (with and without flagging them as a no-show)
* Edit shift info
* Mark whether a volunteer attended their shift
* Respond to questions/concerns of volunteers
* Ban a volunteer (and record a reason) from
    - A role
    - All roles
* View all volunteers that have signed up for a session
* Approve a volunteer as trained for a role
* Contact:
    - All volunteers
    - All volunteers with certain training
    - All volunteers who have signed up for a free shift
    - All volunteers who have indicated that they may do cover shifts
* View which volunteers are currently in which shifts
* View which current shifts require volunteers
* View which upcoming shifts require volunteers

As an admin I would like to:
----------------------------
* Create roles with
    - Any requirements (e.g. age)
    - A list of trainers
    - Minimum/maximum number of volunteers required per shift
    - A description
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

It would be nice to have:
-------------------------
* Schedule integration
* APIs for:
    - Individual's alerts
    - General alerts
    - The data set
