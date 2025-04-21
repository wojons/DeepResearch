// Main JavaScript for DeepResearch Viewer

document.addEventListener('DOMContentLoaded', () => {
    // Initialize the application
    initApp();
});

/**
 * Initialize the application
 */
async function initApp() {
    try {
        // Fetch the research index data
        const projects = await fetchResearchIndex();
        
        // Populate the project list
        populateProjectList(projects);
        
        // Set up event listeners
        setupEventListeners();
    } catch (error) {
        console.error('Error initializing app:', error);
        document.getElementById('project-list').innerHTML = `
            <div class="error">Error loading projects: ${error.message}</div>
        `;
    }
}

/**
 * Get the research index data
 * @returns {Promise<Array>} Array of project objects
 */
async function fetchResearchIndex() {
    // NOTE: Using hardcoded data to avoid CORS issues when opening the file directly
    // For production use, this should be replaced with a fetch request when served from a proper web server
    
    // Hardcoded data from research_index.json
    const researchData = [
        {
            "taskName": "AI_YouTube_Script_Techniques",
            "path": "./AI_YouTube_Script_Techniques/",
            "title": "Research Task: AI_YouTube_Script_Techniques",
            "date": "2025-04-20",
            "summary": "Identify and summarize the most effective AI-driven techniques and best practices for generating engaging YouTube video scripts. Focus on hooks, tone, structure, overcoming AI writing pitfalls, tool/prompt strategies, and challenges/solutions."
        }
    ];
    
    // Return the data as a resolved promise
    return Promise.resolve(researchData);
    
    /* 
    // Original fetch implementation - uncomment when using a web server
    try {
        const response = await fetch('../research_index.json');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching research index:', error);
        throw error;
    }
    */
}

/**
 * Populate the project list with data from the research index
 * @param {Array} projects Array of project objects
 */
function populateProjectList(projects) {
    const projectListElement = document.getElementById('project-list');
    
    // Clear loading message
    projectListElement.innerHTML = '';
    
    if (projects.length === 0) {
        projectListElement.innerHTML = '<div class="no-projects">No research projects found</div>';
        return;
    }
    
    // Create HTML for each project
    projects.forEach(project => {
        const projectElement = document.createElement('div');
        projectElement.className = 'project-item';
        projectElement.dataset.path = project.path;
        projectElement.dataset.title = project.title;
        projectElement.dataset.date = project.date;
        projectElement.dataset.summary = project.summary;
        
        projectElement.innerHTML = `
            <div class="project-title">${project.title}</div>
            <div class="project-date">${project.date}</div>
        `;
        
        projectListElement.appendChild(projectElement);
    });
}

/**
 * Set up event listeners for the application
 */
function setupEventListeners() {
    // Add click event listener to project list (event delegation)
    document.getElementById('project-list').addEventListener('click', handleProjectClick);
}

/**
 * Handle click events on project items
 * @param {Event} event Click event
 */
async function handleProjectClick(event) {
    // Find the closest project-item element
    const projectElement = event.target.closest('.project-item');
    
    if (!projectElement) return;
    
    // Remove active class from all projects
    document.querySelectorAll('.project-item').forEach(item => {
        item.classList.remove('active');
    });
    
    // Add active class to clicked project
    projectElement.classList.add('active');
    
    // Get project data from dataset
    const path = projectElement.dataset.path;
    const title = projectElement.dataset.title;
    const date = projectElement.dataset.date;
    const summary = projectElement.dataset.summary;
    
    // Update report header
    document.getElementById('report-title').textContent = title;
    document.getElementById('report-date').textContent = `Date: ${date}`;
    document.getElementById('report-summary').textContent = summary;
    
    // Clear previous report content and show loading message
    const reportContentElement = document.getElementById('report-content');
    reportContentElement.textContent = 'Loading report...';
    
    try {
        // Fetch the report.md file
        const reportPath = `${path}report.md`;
        const reportContent = await fetchReportContent(reportPath);
        
        // Display the report content
        reportContentElement.textContent = reportContent;
    } catch (error) {
        console.error('Error fetching report:', error);
        reportContentElement.textContent = `Error loading report: ${error.message}`;
    }
}

/**
 * Get the content of a report.md file
 * @param {string} path Path to the report.md file
 * @returns {Promise<string>} Content of the report.md file
 */
async function fetchReportContent(path) {
    // NOTE: Using mock data to avoid CORS issues when opening the file directly
    // For production use, this should be replaced with a fetch request when served from a proper web server
    
    // Mock report content for demonstration
    const mockReportContent = `# AI YouTube Script Techniques Research Report

## Executive Summary

This research identifies and summarizes the most effective AI-driven techniques and best practices for generating engaging YouTube video scripts. The findings highlight optimal approaches for creating hooks, establishing appropriate tone, structuring content effectively, overcoming common AI writing pitfalls, implementing tool/prompt strategies, and addressing challenges with practical solutions.

## Introduction

YouTube remains the dominant video platform globally, with creators constantly seeking ways to optimize their content for engagement and growth. AI tools have emerged as powerful assistants in the script creation process, offering efficiency and creative support. This research explores how to leverage these AI capabilities most effectively while maintaining authenticity and audience connection.

*This is a mock report for demonstration purposes. The actual report would contain much more detailed content.*`;
    
    // Return the mock data as a resolved promise
    return Promise.resolve(mockReportContent);
    
    /* 
    // Original fetch implementation - uncomment when using a web server
    try {
        const response = await fetch(`../${path}report.md`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const text = await response.text();
        return text;
    } catch (error) {
        console.error('Error fetching report content:', error);
        throw error;
    }
    */
}
