// Script to upgrade all stripe files with new UI components
// This will be executed manually to update each file

const fs = require('fs');
const path = require('path');

const stripeFiles = [
    'white-belt-stripe1-carousel-NEW.html',
    'white-belt-stripe2-carousel-NEW.html',
    'white-belt-stripe3-carousel-NEW.html',
    'white-belt-stripe4-carousel-NEW.html',
    'blue-belt-stripe1-carousel-NEW.html',
    'blue-belt-stripe2-carousel-NEW.html',
    'blue-belt-stripe3-carousel-NEW.html',
    'blue-belt-stripe4-carousel-NEW.html',
    'purple-belt-stripe1-carousel-NEW.html',
    'purple-belt-stripe2-carousel-NEW.html',
    'purple-belt-stripe3-carousel-NEW.html',
    'purple-belt-stripe4-carousel-NEW.html',
    'brown-belt-stripe1-carousel-NEW.html'
];

console.log('Stripe files to upgrade:', stripeFiles.length);


