create table if not exists academy_basic_exam_emails
(
    id         int unsigned auto_increment
        primary key,
    attempt_id int       not null,
    student_id int       not null,
    created_at timestamp null,
    updated_at timestamp null
)
    collate = utf8mb3_unicode_ci;

create table if not exists academy_exam_assignments
(
    id                  int unsigned auto_increment
        primary key,
    student_id          int          not null,
    instructor_id       int          not null,
    moodle_uid          int          not null,
    course_id           int          not null,
    course_name         varchar(255) not null,
    quiz_id             int          not null,
    rating_id           int          not null,
    attempt_emails_sent varchar(255) null,
    created_at          timestamp    null,
    updated_at          timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists action_log
(
    id         int auto_increment
        primary key,
    `from`     int      not null,
    `to`       int      not null,
    log        text     not null,
    created_at datetime not null,
    updated_at datetime not null
)
    charset = latin1;

create table if not exists api_log
(
    id       bigint unsigned auto_increment
        primary key,
    facility varchar(3)   not null,
    datetime datetime     not null,
    method   varchar(7)   not null,
    url      varchar(255) not null,
    data     varchar(255) not null
)
    charset = latin1;

create index facility
    on api_log (facility);

create table if not exists checklist_data
(
    id           int unsigned auto_increment
        primary key,
    checklist_id int unsigned not null,
    item         varchar(255) not null,
    `order`      int unsigned not null,
    created_at   datetime     not null,
    updated_at   datetime     not null
)
    charset = latin1;

create table if not exists checklists
(
    id         int unsigned auto_increment
        primary key,
    name       varchar(255) not null,
    active     int          not null,
    `order`    int unsigned not null,
    created_at datetime     not null,
    updated_at datetime     not null
)
    charset = latin1;

create table if not exists controller_training
(
    id             int unsigned auto_increment
        primary key,
    student_cid    int unsigned                                                           not null,
    instructor_cid int unsigned                                                           not null,
    facility       varchar(3)                                                             not null,
    position       varchar(10)                                                            not null,
    type           enum ('Classroom', 'Live', 'Simulation', 'OTS Live', 'OTS Simulation') not null,
    checklist_name varchar(255)                                                           not null,
    checklist_data mediumtext                                                             not null,
    created_at     datetime                                                               not null,
    updated_at     datetime                                                               not null
)
    charset = latin1;

create table if not exists controllers
(
    cid                     int unsigned         not null,
    fname                   varchar(100)         not null,
    lname                   varchar(100)         not null,
    email                   varchar(255)         not null,
    facility                varchar(4)           not null,
    rating                  int                  not null,
    created_at              datetime             null,
    updated_at              datetime             not null,
    flag_needbasic          int        default 0 not null,
    flag_xferOverride       int        default 0 not null,
    facility_join           datetime             not null,
    flag_homecontroller     int                  not null,
    remember_token          varchar(255)         null,
    cert_update             int        default 0 not null,
    lastactivity            datetime             not null,
    flag_broadcastOptedIn   tinyint(1) default 0 not null,
    flag_preventStaffAssign tinyint(1) default 0 not null,
    access_token            mediumtext           null,
    refresh_token           mediumtext           null,
    token_expires           bigint unsigned      null,
    discord_id              varchar(255)         null,
    prefname                tinyint(1)           not null,
    prefname_date           datetime             null,
    constraint cid_2
        unique (cid),
    constraint controllers_discord_id_unique
        unique (discord_id)
)
    collate = utf8mb4_unicode_ci;

create index cid
    on controllers (cid);

create index facility
    on controllers (facility);

create index fname
    on controllers (fname);

create index lname
    on controllers (lname);

create index rating
    on controllers (rating);

create table if not exists email_accounts
(
    id         int unsigned auto_increment
        primary key,
    facility   varchar(255) not null,
    username   varchar(255) not null,
    cid        int          not null,
    created_at timestamp    null,
    updated_at timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists email_config
(
    address     text null,
    config      text null,
    destination text null,
    modified_by int  null,
    updated_at  text null
);

create table if not exists email_templates
(
    id          int unsigned auto_increment
        primary key,
    facility_id varchar(255) not null,
    template    varchar(255) not null,
    body        text         not null,
    created_at  timestamp    null,
    updated_at  timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists exam_assignments
(
    id            bigint unsigned auto_increment
        primary key,
    cid           int unsigned not null,
    exam_id       int unsigned not null,
    instructor_id int unsigned not null,
    assigned_date datetime     not null,
    expire_date   datetime     not null
)
    charset = latin1;

create index cid
    on exam_assignments (cid, exam_id);

create table if not exists exam_generated
(
    id          int unsigned auto_increment
        primary key,
    cid         int unsigned not null,
    exam_id     int unsigned not null,
    question_id int unsigned not null
)
    charset = latin1;

create table if not exists exam_questions
(
    id       int unsigned auto_increment
        primary key,
    exam_id  int unsigned not null,
    question text         not null,
    type     int          not null comment '0 - multiple choice, 1 - true/false',
    answer   varchar(255) not null,
    alt1     varchar(255) not null,
    alt2     varchar(255) not null,
    alt3     varchar(255) not null,
    notes    varchar(255) null
)
    charset = latin1;

create table if not exists exam_reassignments
(
    id            bigint unsigned auto_increment
        primary key,
    cid           int unsigned not null,
    exam_id       int unsigned not null,
    reassign_date datetime     not null,
    instructor_id int unsigned not null
)
    charset = latin1;

create table if not exists exam_results
(
    id        bigint unsigned auto_increment
        primary key,
    exam_id   bigint unsigned not null,
    exam_name varchar(255)    not null,
    cid       int             not null,
    score     int             not null,
    passed    int             not null,
    date      datetime        not null
)
    charset = latin1;

create table if not exists exam_results_data
(
    id         int unsigned auto_increment
        primary key,
    result_id  bigint unsigned not null,
    question   varchar(255)    not null,
    correct    varchar(255)    not null,
    selected   varchar(255)    null,
    notes      varchar(255)    not null,
    is_correct int             not null
)
    charset = latin1;

create table if not exists exams
(
    id                int unsigned auto_increment
        primary key,
    facility_id       varchar(4)                                      not null,
    name              varchar(255)                                    not null,
    number            int                                             not null,
    is_active         int             default 1                       not null comment '0 - no, 1 - yes',
    cbt_required      bigint unsigned default '0'                     null,
    retake_period     int             default 7                       not null comment 'number of days',
    passing_score     int             default 70                      not null,
    answer_visibility enum ('none', 'user_only', 'all', 'all_passed') not null
)
    charset = latin1;

create table if not exists facilities
(
    id                  char(3)       not null,
    name                varchar(255)  not null,
    url                 varchar(255)  not null,
    hosted_email_domain varchar(255)  null,
    region              int           not null,
    atm                 int unsigned  not null,
    datm                int unsigned  not null,
    ta                  int unsigned  not null,
    ec                  int unsigned  not null,
    fe                  int unsigned  not null,
    wm                  int unsigned  not null,
    uls_return          varchar(255)  not null,
    uls_devreturn       varchar(255)  not null,
    uls_secret          varchar(255)  not null,
    uls_jwk             text          null,
    active              int default 1 not null,
    apikey              varchar(25)   not null,
    ip                  varchar(128)  not null,
    api_sandbox_key     varchar(255)  not null,
    api_sandbox_ip      varchar(128)  not null,
    apiv2_jwk           text          null,
    welcome_text        mediumtext    not null,
    ace                 int           not null,
    apiv2_jwk_dev       text          null,
    uls_jwk_dev         varchar(255)  not null,
    url_dev             varchar(255)  not null,
    constraint id
        unique (id)
)
    comment 'Facility (ARTCC/CF/FIR) Listing' charset = latin1;

create table if not exists facility_trends
(
    id       bigint unsigned auto_increment
        primary key,
    date     date       not null,
    facility varchar(4) not null,
    obs      int        not null,
    obsg30   int        not null,
    s1       int        not null,
    s2       int        not null,
    s3       int        not null,
    c1       int        not null,
    c3       int        not null,
    i1       int        not null comment 'I1 or greater'
)
    charset = latin1;

create table if not exists flights
(
    callsign char(10)    not null,
    lat      varchar(15) not null,
    `long`   varchar(15) not null,
    hdg      int         not null,
    dest     varchar(4)  not null,
    dep      varchar(4)  not null,
    type     varchar(8)  not null,
    constraint callsign
        unique (callsign)
)
    collate = utf8mb3_unicode_ci;

create table if not exists jobs
(
    id         int unsigned auto_increment
        primary key,
    type       varchar(255)                                     not null,
    data       mediumtext                                       not null,
    status     enum ('pending', 'running', 'success', 'failed') not null,
    created_at timestamp                                        null,
    updated_at timestamp                                        null
)
    collate = utf8mb3_unicode_ci;

create table if not exists knowledgebase_categories
(
    id         int unsigned auto_increment
        primary key,
    name       varchar(256) not null,
    created_at datetime     not null,
    updated_at datetime     not null
)
    charset = latin1;

create table if not exists knowledgebase_questions
(
    id          int unsigned auto_increment
        primary key,
    category_id int unsigned not null,
    `order`     int unsigned not null,
    question    text         not null,
    answer      mediumtext   not null,
    updated_by  int          not null,
    created_at  datetime     not null,
    updated_at  datetime     not null
)
    charset = latin1;

create table if not exists login_tokens
(
    token     varchar(255)                        not null,
    cid       int unsigned                        not null,
    timestamp timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    ip        varchar(128)                        not null,
    constraint token
        unique (token)
)
    charset = latin1;

create table if not exists memberships
(
    cid         int unsigned not null
        primary key,
    rating      int unsigned not null,
    facility_id varchar(3)   not null,
    type        int          not null comment '1 - Home, 2- Visitor',
    joined      datetime     not null
)
    comment 'Defines roster of facilities' charset = latin1;

create table if not exists migrations
(
    id        int unsigned null,
    migration varchar(255) not null,
    batch     int          not null
)
    collate = utf8mb3_unicode_ci;

create table if not exists oauth_clients
(
    id            bigint unsigned auto_increment,
    name          varchar(191) not null,
    client_id     varchar(128) null,
    client_secret varchar(255) null,
    redirect_uris text         null,
    created_at    datetime(3)  null,
    updated_at    datetime(3)  null,
    primary key (id, name)
);

create table if not exists oauth_logins
(
    id                    bigint unsigned auto_increment
        primary key,
    token                 varchar(128)    null,
    code                  longtext        null,
    user_agent            varchar(255)    null,
    redirect_uri          varchar(255)    null,
    client_id             bigint unsigned null,
    state                 longtext        null,
    code_challenge        longtext        null,
    code_challenge_method longtext        null,
    scope                 longtext        null,
    c_id                  bigint unsigned null,
    created_at            datetime(3)     null,
    updated_at            datetime(3)     null,
    constraint fk_oauth_logins_client
        foreign key (client_id) references oauth_clients (id)
);

create table if not exists ots_evals_forms
(
    id               int unsigned auto_increment
        primary key,
    name             varchar(255)         not null,
    rating_id        int                  not null,
    position         varchar(255)         not null,
    instructor_notes text                 null,
    is_statement     tinyint(1) default 0 not null,
    description      text                 not null,
    active           tinyint(1) default 1 not null,
    created_at       timestamp            null,
    updated_at       timestamp            null,
    constraint ots_evals_forms_name_unique
        unique (name)
)
    collate = utf8mb3_unicode_ci;

create table if not exists ots_evals
(
    id                 int unsigned auto_increment
        primary key,
    training_record_id int          null,
    student_id         int          not null,
    instructor_id      int          not null,
    facility_id        varchar(255) not null,
    exam_position      varchar(255) not null,
    form_id            int unsigned not null,
    notes              text         null,
    exam_date          date         not null,
    result             tinyint(1)   not null,
    signature          text         not null,
    created_at         timestamp    null,
    updated_at         timestamp    null,
    constraint ots_evals_form_id_foreign
        foreign key (form_id) references ots_evals_forms (id)
            on delete cascade
)
    collate = utf8mb3_unicode_ci;

create table if not exists ots_evals_perf_cats
(
    id         int unsigned auto_increment
        primary key,
    label      varchar(255) not null,
    form_id    int unsigned not null,
    `order`    int          not null,
    created_at timestamp    null,
    updated_at timestamp    null,
    constraint ots_evals_perf_cats_form_id_foreign
        foreign key (form_id) references ots_evals_forms (id)
            on delete cascade
)
    collate = utf8mb3_unicode_ci;

create table if not exists ots_evals_perf_indicators
(
    id             int unsigned auto_increment
        primary key,
    perf_cat_id    int unsigned       not null,
    label          varchar(255)       not null,
    help_text      text               null,
    header_type    smallint default 0 not null,
    is_commendable tinyint(1)         null,
    is_required    tinyint(1)         null,
    can_unsat      tinyint(1)         null,
    `order`        int                not null,
    extra_options  varchar(255)       null,
    updated_at     timestamp          null,
    created_at     timestamp          null,
    constraint ots_evals_perf_indicators_perf_cat_id_foreign
        foreign key (perf_cat_id) references ots_evals_perf_cats (id)
            on delete cascade
)
    collate = utf8mb3_unicode_ci;

create table if not exists ots_evals_indicator_results
(
    id                int unsigned auto_increment
        primary key,
    perf_indicator_id int unsigned not null,
    eval_id           int unsigned not null,
    result            smallint     not null,
    comment           varchar(255) null,
    created_at        timestamp    null,
    updated_at        timestamp    null,
    constraint ots_evals_indicator_results_eval_id_foreign
        foreign key (eval_id) references ots_evals (id)
            on delete cascade,
    constraint ots_evals_indicator_results_perf_indicator_id_foreign
        foreign key (perf_indicator_id) references ots_evals_perf_indicators (id)
            on delete cascade
)
    collate = utf8mb3_unicode_ci;

create table if not exists password_resets
(
    email      varchar(255)                            not null,
    token      varchar(255)                            not null,
    created_at timestamp default '0000-00-00 00:00:00' not null
)
    collate = utf8mb3_unicode_ci;

create index password_resets_email_index
    on password_resets (email);

create index password_resets_token_index
    on password_resets (token);

create table if not exists policy_categories
(
    id         int unsigned auto_increment
        primary key,
    name       varchar(255)      not null,
    `order`    smallint unsigned not null,
    created_at timestamp         null,
    updated_at timestamp         null
)
    collate = utf8mb3_unicode_ci;

create table if not exists policies
(
    id             int unsigned auto_increment
        primary key,
    ident          varchar(255)      not null,
    category       int unsigned      not null,
    title          text              not null,
    slug           varchar(255)      not null,
    description    varchar(255)      not null,
    extension      varchar(255)      not null,
    effective_date date              null,
    perms          varchar(255)      not null,
    visible        tinyint(1)        not null,
    `order`        smallint unsigned not null,
    created_at     timestamp         null,
    updated_at     timestamp         null,
    constraint policies_category_foreign
        foreign key (category) references policy_categories (id)
            on delete cascade
)
    collate = utf8mb3_unicode_ci;

create table if not exists promotions
(
    id         int auto_increment
        primary key,
    cid        int          not null,
    grantor    int unsigned not null,
    `to`       int          not null,
    `from`     int          not null,
    created_at datetime     not null,
    updated_at datetime     not null,
    exam       date         not null,
    examiner   int unsigned not null,
    position   varchar(11)  not null,
    eval_id    int unsigned null
)
    charset = latin1;

create table if not exists promotionstest
(
    id         int auto_increment
        primary key,
    cid        int          not null,
    grantor    int unsigned not null,
    `to`       int          not null,
    `from`     int          not null,
    created_at datetime     not null,
    updated_at datetime     not null,
    exam       date         not null,
    examiner   int unsigned not null,
    position   varchar(11)  not null
)
    charset = latin1;

create table if not exists push_log
(
    id           int auto_increment
        primary key,
    created_at   timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    updated_at   date                                null,
    title        text                                not null,
    message      text                                not null,
    submitted_by text                                not null
)
    charset = latin1;

create table if not exists ratings
(
    id     int         not null
        primary key,
    short  varchar(3)  not null,
    `long` varchar(18) not null
)
    charset = latin1;

create table if not exists return_paths
(
    id          int unsigned auto_increment
        primary key,
    `order`     int          not null,
    facility_id varchar(255) not null,
    url         varchar(255) not null,
    created_at  timestamp    null,
    updated_at  timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists role_titles
(
    role  varchar(12)  not null,
    title varchar(128) not null,
    constraint role
        unique (role)
)
    charset = latin1;

create table if not exists roles
(
    id         bigint unsigned auto_increment
        primary key,
    cid        int unsigned                        not null,
    facility   varchar(3)                          not null,
    role       varchar(12)                         not null,
    created_at timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP
)
    charset = latin1;

create table if not exists sessions
(
    id            varchar(255) not null,
    user_id       int unsigned null,
    ip_address    varchar(45)  null,
    user_agent    text         null,
    payload       text         not null,
    last_activity int          not null,
    constraint sessions_id_unique
        unique (id)
)
    collate = utf8mb3_unicode_ci;

create table if not exists solo_certs
(
    id         int unsigned auto_increment
        primary key,
    cid        int unsigned                            not null,
    position   varchar(255)                            not null,
    expires    date                                    not null,
    created_at timestamp default '0000-00-00 00:00:00' not null,
    updated_at timestamp default '0000-00-00 00:00:00' not null
)
    collate = utf8mb3_unicode_ci;

create table if not exists stats_archive
(
    id   bigint auto_increment
        primary key,
    date date       not null,
    data mediumtext not null
)
    charset = utf8mb3;

create table if not exists survey_assignments
(
    id         varchar(255) not null,
    survey_id  int          not null,
    facility   varchar(255) not null,
    rating     int          not null,
    misc_data  varchar(255) not null,
    completed  int          not null,
    created_at timestamp    null,
    updated_at timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists survey_questions
(
    id         int unsigned auto_increment
        primary key,
    survey_id  int          not null,
    question   varchar(255) not null,
    data       varchar(255) not null,
    `order`    int          not null,
    created_at timestamp    null,
    updated_at timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists survey_submissions
(
    id          int unsigned auto_increment
        primary key,
    survey_id   int          not null,
    question_id int          not null,
    response    varchar(255) not null,
    facility    varchar(255) not null,
    rating      int          not null,
    created_at  timestamp    null,
    updated_at  timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists surveys
(
    id         int unsigned auto_increment
        primary key,
    facility   varchar(255) not null,
    name       varchar(255) not null,
    created_at timestamp    null,
    updated_at timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists tickets
(
    id          int unsigned auto_increment
        primary key,
    cid         int                                    not null,
    subject     varchar(255)                           not null,
    body        mediumtext                             not null,
    status      enum ('Open', 'Closed')                not null,
    facility    char(3)                                not null,
    assigned_to varchar(255)                           not null,
    notes       mediumtext                             not null,
    priority    enum ('Low', 'Normal', 'High')         not null,
    created_at  datetime default '0000-00-00 00:00:00' not null,
    updated_at  datetime default '0000-00-00 00:00:00' not null
)
    collate = utf8mb3_unicode_ci;

create table if not exists tickets_history
(
    id         bigint unsigned auto_increment
        primary key,
    ticket_id  bigint unsigned not null,
    entry      mediumtext      not null,
    created_at datetime        not null,
    updated_at datetime        not null
)
    charset = latin1;

create index ticket_id
    on tickets_history (ticket_id);

create table if not exists tickets_notes
(
    id         int unsigned auto_increment
        primary key,
    ticket_id  int                                     not null,
    cid        int                                     not null,
    note       mediumtext                              not null,
    created_at timestamp default '0000-00-00 00:00:00' not null,
    updated_at timestamp default '0000-00-00 00:00:00' not null
)
    collate = utf8mb3_unicode_ci;

create table if not exists tickets_replies
(
    id         int unsigned auto_increment
        primary key,
    ticket_id  int                                     not null,
    cid        int                                     not null,
    body       mediumtext                              not null,
    created_at timestamp default '0000-00-00 00:00:00' not null,
    updated_at timestamp default '0000-00-00 00:00:00' not null
)
    collate = utf8mb3_unicode_ci;

create table if not exists tmu_colors
(
    id     varchar(4) not null,
    black  text       null,
    brown  text       null comment '1',
    blue   text       null comment '2',
    gray   text       null comment '3',
    green  text       null comment '4',
    lime   text       null comment '5',
    cyan   text       null comment '6',
    orange text       null comment '7',
    red    text       null comment '9',
    purple text       null comment '10',
    white  text       null comment '11',
    yellow text       null comment '12',
    violet text       null comment '13',
    guide  text       null,
    constraint id
        unique (id)
)
    charset = utf8mb3;

create table if not exists tmu_facilities
(
    id     varchar(4)   not null,
    parent varchar(4)   null,
    name   varchar(255) not null,
    coords text         not null,
    constraint id
        unique (id)
)
    charset = latin1;

create table if not exists tmu_notices
(
    id              int unsigned auto_increment
        primary key,
    tmu_facility_id varchar(255) not null,
    priority        smallint     not null,
    message         varchar(255) not null,
    start_date      datetime     not null,
    expire_date     datetime     null,
    created_at      timestamp    null,
    updated_at      timestamp    null,
    is_delay        tinyint(1)   not null,
    is_pref_route   tinyint(1)   not null
)
    collate = utf8mb3_unicode_ci;

create table if not exists training_blocks
(
    id       bigint unsigned auto_increment
        primary key,
    facility varchar(3)                                                            not null comment 'Facility ID, ZAE = VATUSA Academy',
    `order`  int                                                                   not null,
    name     varchar(255)                                                          not null,
    level    enum ('Senior Staff', 'Staff', 'I1', 'C1', 'S1', 'ALL') default 'ALL' not null,
    visible  tinyint(1)                                              default 1     not null
)
    charset = latin1;

create table if not exists training_chapters
(
    id      bigint unsigned auto_increment
        primary key,
    blockid bigint unsigned not null,
    `order` int             not null,
    name    varchar(255)    not null,
    url     varchar(255)    not null,
    visible tinyint(1)      not null,
    constraint training_chapters_ibfk_1
        foreign key (blockid) references training_blocks (id)
            on update cascade on delete cascade
)
    charset = latin1;

create index blockid
    on training_chapters (blockid);

create table if not exists training_progress
(
    cid       int unsigned    not null,
    chapterid bigint unsigned not null,
    date      datetime        not null,
    constraint training_progress_ibfk_1
        foreign key (chapterid) references training_chapters (id)
            on update cascade on delete cascade
)
    charset = latin1;

create index chapterid
    on training_progress (chapterid);

create table if not exists training_records
(
    id            int unsigned auto_increment
        primary key,
    student_id    int          not null,
    instructor_id int          not null,
    session_date  datetime     not null,
    facility_id   varchar(255) not null,
    position      varchar(255) not null,
    duration      time         not null,
    movements     int          null,
    score         int          null,
    notes         text         not null,
    location      smallint     not null,
    ots_status    smallint     not null,
    ots_eval_id   int          null,
    is_cbt        tinyint(1)   not null,
    solo_granted  tinyint(1)   not null,
    modified_by   int          null,
    created_at    timestamp    null,
    updated_at    timestamp    null
)
    collate = utf8mb3_unicode_ci;

create table if not exists transfers
(
    id         int unsigned auto_increment
        primary key,
    cid        int unsigned not null,
    `to`       varchar(3)   not null,
    `from`     varchar(3)   not null,
    reason     text         not null,
    status     int          not null comment '0-pending,1-accepted,2-rejected',
    actiontext text         not null,
    actionby   int unsigned not null,
    created_at datetime     not null,
    updated_at datetime     not null
)
    charset = latin1;

create index cid
    on transfers (cid, created_at);

create index created_at
    on transfers (created_at);

create table if not exists uls_tokens
(
    facility varchar(4)    not null,
    token    varchar(128)  not null
        primary key,
    date     datetime      not null,
    ip       varchar(128)  not null,
    cid      int unsigned  not null,
    expired  int default 0 not null
)
    charset = latin1;

create table if not exists users
(
    id             int unsigned auto_increment
        primary key,
    name           varchar(255)                            not null,
    email          varchar(255)                            not null,
    password       varchar(60)                             not null,
    remember_token varchar(100)                            null,
    created_at     timestamp default '0000-00-00 00:00:00' not null,
    updated_at     timestamp default '0000-00-00 00:00:00' not null,
    constraint users_email_unique
        unique (email)
)
    collate = utf8mb3_unicode_ci;

create table if not exists visits
(
    id         bigint unsigned auto_increment
        primary key,
    cid        int unsigned not null,
    facility   varchar(3)   not null,
    created_at timestamp    null,
    updated_at timestamp    null
)
    collate = utf8mb3_unicode_ci;

