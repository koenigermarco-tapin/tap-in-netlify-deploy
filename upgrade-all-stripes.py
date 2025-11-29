#!/usr/bin/env python3
"""
Upgrade all 13 stripe files with:
1. Scenario Question Renderer
2. Multiple Choice Renderer
3. Milestone Celebrations
4. Achievement Badge System
5. Fun Facts Display
6. Standardize Question Counts
"""

import re
import os

STRIPE_FILES = [
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
]

# CSS for new features
SCENARIO_CSS = """
        /* Scenario Question Styles */
        .scenario-options {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin: 20px 0;
        }
        .scenario-option {
            background: #f8f9fa;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 15px 20px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }
        .scenario-option:hover {
            border-color: #667eea;
            background: #f0f0ff;
            transform: translateX(5px);
        }
        .scenario-option.selected {
            border-color: #667eea;
            background: #e8e8ff;
        }
        .scenario-option.correct {
            border-color: #10b981;
            background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        }
        .scenario-option.correct .option-letter {
            background: #10b981;
        }
        .scenario-option.incorrect {
            border-color: #ef4444;
            background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        }
        .scenario-option.incorrect .option-letter {
            background: #ef4444;
        }
        .scenario-option.neutral {
            border-color: #f59e0b;
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        }
        .scenario-option.neutral .option-letter {
            background: #f59e0b;
        }
        .option-letter {
            background: #667eea;
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.2rem;
            flex-shrink: 0;
            transition: all 0.2s;
        }
        .option-text {
            color: #333;
            line-height: 1.6;
            font-size: 1rem;
            padding-top: 8px;
        }
        .scenario-feedback {
            margin-top: 20px;
            animation: fadeIn 0.3s ease;
        }
        .scenario-insight {
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            border-left: 4px solid #3b82f6;
        }
        @media (max-width: 768px) {
            .scenario-option {
                padding: 12px 15px;
                gap: 12px;
            }
            .option-letter {
                width: 32px;
                height: 32px;
                font-size: 1rem;
            }
            .option-text {
                font-size: 0.9rem;
            }
        }
"""

MULTIPLE_CHOICE_CSS = """
        /* Multiple Choice Styles */
        .mc-options {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin: 20px 0;
        }
        .mc-option {
            background: #ffffff;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 18px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }
        .mc-option:hover {
            border-color: #667eea;
            background: #fafbff;
            transform: translateX(3px);
        }
        .mc-option.selected {
            border-color: #667eea;
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
        }
        .mc-radio {
            padding-top: 2px;
        }
        .mc-radio input[type="radio"] {
            width: 20px;
            height: 20px;
            accent-color: #667eea;
            cursor: pointer;
        }
        .mc-content {
            flex: 1;
        }
        .mc-text {
            color: #333;
            line-height: 1.6;
            font-size: 1rem;
            margin-bottom: 6px;
        }
        .mc-type {
            color: #667eea;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .mc-feedback {
            margin-top: 20px;
            animation: fadeIn 0.3s ease;
        }
        .mc-insight {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border-left: 4px solid #10b981;
        }
        .mc-type-badge {
            display: inline-block;
            background: #10b981;
            color: white;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        @media (max-width: 768px) {
            .mc-option {
                padding: 15px;
            }
            .mc-text {
                font-size: 0.9rem;
            }
        }
"""

MILESTONE_CSS = """
        @keyframes scaleIn {
            from {
                opacity: 0;
                transform: scale(0.8);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        @keyframes confettiFall {
            to {
                transform: translateY(100vh) rotate(360deg) translateX(200px);
                opacity: 0;
            }
        }
        .milestone-content button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .fun-fact-box {
            animation: slideIn 0.4s ease;
        }
"""

print(f"Found {len(STRIPE_FILES)} stripe files to upgrade")


