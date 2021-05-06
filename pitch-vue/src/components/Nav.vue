<template>
<div id=navbar>
    <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand>Pitch</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
            <b-nav-item href="/pitch">Home</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav>
            <b-nav-item href="/pitch/courses">Courses</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
            <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>

            <b-navbar-nav right>
                <b-nav-item href="/pitch/login">Log in</b-nav-item>
            </b-navbar-nav>
        </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</div>
</template>

<style>
</style>
