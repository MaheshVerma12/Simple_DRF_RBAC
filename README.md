# A minimal Django DRF Permissions Project

This project is a Django REST Framework application that demonstrates a robust permissions system for a project management tool. It includes role-based access control for users (Admin, Manager, Developer), project and task management, and a notification system.

## Features

*   **User Roles:** Admin, Manager, and Developer roles with distinct permissions.
*   **Project Management:** Create, view, update, and delete projects.
*   **Task Management:** Create, view, update, and delete tasks within projects.
*   **Task Assignment:** Assign tasks to developers.
*   **Notifications:** Users receive notifications for important events.
*   **Comments:** Users can comment on tasks.
*   **Custom Permissions:** Granular control over who can perform which actions.
*   **API Endpoints:** A comprehensive set of API endpoints for all features.

## Usage

After starting the server, you can access the API endpoints at `http://127.0.0.1:8000/api/`.

## API Endpoints

*   `/api/projects/`
*   `/api/tasks/`
*   `/api/tasklogs/`
*   `/api/notifications/`
*   `/api/comments/`

## Permissions

*   **Admin:** Can perform any action on any resource.
*   **Manager:** Can create projects and manage tasks within their projects.
*   **Developer:** Can view projects they are a part of and view and update tasks assigned to them.
