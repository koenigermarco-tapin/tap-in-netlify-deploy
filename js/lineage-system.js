/**
 * Lineage & Team Leaderboard System
 * BJJ-style referral tracking with gym/team competition
 * Phase 1: Basic Referrals + Lineage Tracking
 */

(function() {
  'use strict';

  // ============================================
  // GENERATE REFERRAL CODE
  // ============================================
  function generateReferralCode(userName = 'User') {
    // Check if user already has a code
    const existing = localStorage.getItem('userReferralCode');
    if (existing) return existing;

    // Generate unique code: NAME-RANDOM
    const nameSlug = userName
      .toLowerCase()
      .replace(/[^a-z0-9]/g, '')
      .substring(0, 10) || 'user';

    const randomSuffix = Math.random().toString(36).substring(2, 6).toUpperCase();
    const code = `${nameSlug}-${randomSuffix}`;

    // Save to localStorage
    localStorage.setItem('userReferralCode', code);
    return code;
  }

  // ============================================
  // GET USER REFERRAL CODE
  // ============================================
  function getUserReferralCode() {
    return localStorage.getItem('userReferralCode') || generateReferralCode();
  }

  // ============================================
  // CREATE REFERRAL LINK
  // ============================================
  function createReferralLink(referralCode = null) {
    const code = referralCode || getUserReferralCode();
    const baseUrl = window.location.origin;
    const landingPage = 'index-DUAL-ENTRY.html'; // Main entry point
    return `${baseUrl}/${landingPage}?ref=${code}`;
  }

  // ============================================
  // GET REFERRER FROM URL
  // ============================================
  function getReferrerFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('ref');
  }

  // ============================================
  // TRACK REFERRAL ON SIGNUP/START
  // ============================================
  function trackReferralOnStart() {
    const referrerCode = getReferrerFromURL();
    if (!referrerCode) return null;

    // Store in sessionStorage for later use
    sessionStorage.setItem('referredBy', referrerCode);

    // Get or create user's own code
    const myCode = getUserReferralCode();

    // Build lineage chain
    const lineage = getLineageChain(referrerCode);
    lineage.push(referrerCode); // Add referrer
    lineage.push(myCode); // Add self

    // Save user data
    const userData = {
      userId: generateUserId(),
      referralCode: myCode,
      referredBy: referrerCode,
      referralLineage: lineage,
      joinedDate: new Date().toISOString(),
      personalXP: 0,
      currentBelt: 'White'
    };

    saveUserData(userData);

    // Update referrer's student count
    incrementStudentCount(referrerCode);

    return userData;
  }

  // ============================================
  // GET LINEAGE CHAIN
  // ============================================
  function getLineageChain(referrerCode) {
    // Get referrer's data
    const referrerData = getUserDataByCode(referrerCode);
    if (!referrerData) return [];

    // Build chain: [grandmaster, master, instructor, ...]
    const chain = referrerData.referralLineage || [];
    return [...chain, referrerCode];
  }

  // ============================================
  // SAVE USER DATA
  // ============================================
  function saveUserData(userData) {
    const users = getAllUsers();
    users[userData.userId] = userData;
    localStorage.setItem('lineageUsers', JSON.stringify(users));
    localStorage.setItem('currentUserId', userData.userId);
  }

  // ============================================
  // GET USER DATA
  // ============================================
  function getUserData() {
    const userId = localStorage.getItem('currentUserId');
    if (!userId) {
      // Create new user
      const code = getUserReferralCode();
      const userData = {
        userId: generateUserId(),
        referralCode: code,
        referredBy: null,
        referralLineage: [],
        joinedDate: new Date().toISOString(),
        personalXP: parseInt(localStorage.getItem('totalXP') || '0'),
        currentBelt: getCurrentBelt()
      };
      saveUserData(userData);
      return userData;
    }

    const users = getAllUsers();
    return users[userId] || null;
  }

  // ============================================
  // GET USER DATA BY REFERRAL CODE
  // ============================================
  function getUserDataByCode(referralCode) {
    const users = getAllUsers();
    for (const userId in users) {
      if (users[userId].referralCode === referralCode) {
        return users[userId];
      }
    }
    return null;
  }

  // ============================================
  // GET ALL USERS
  // ============================================
  function getAllUsers() {
    const stored = localStorage.getItem('lineageUsers');
    return stored ? JSON.parse(stored) : {};
  }

  // ============================================
  // GENERATE USER ID
  // ============================================
  function generateUserId() {
    return 'user_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
  }

  // ============================================
  // GET CURRENT BELT
  // ============================================
  function getCurrentBelt() {
    // Check localStorage for belt progression
    if (localStorage.getItem('blackBeltStripe4Complete')) return 'Black';
    if (localStorage.getItem('brownBeltStripe4Complete')) return 'Brown';
    if (localStorage.getItem('purpleBeltStripe4Complete')) return 'Purple';
    if (localStorage.getItem('blueBeltStripe4Complete')) return 'Blue';
    return 'White';
  }

  // ============================================
  // INCREMENT STUDENT COUNT
  // ============================================
  function incrementStudentCount(referrerCode) {
    const referrer = getUserDataByCode(referrerCode);
    if (!referrer) return;

    referrer.studentsCount = (referrer.studentsCount || 0) + 1;
    saveUserData(referrer);

    // Update lineage counts recursively
    updateLineageCounts(referrer.referralLineage);
  }

  // ============================================
  // UPDATE LINEAGE COUNTS
  // ============================================
  function updateLineageCounts(lineage) {
    lineage.forEach(code => {
      const user = getUserDataByCode(code);
      if (user) {
        user.lineageCount = (user.lineageCount || 0) + 1;
        saveUserData(user);
      }
    });
  }

  // ============================================
  // GET DIRECT STUDENTS
  // ============================================
  function getDirectStudents(userId = null) {
    const currentUser = userId ? getUserDataByCode(userId) : getUserData();
    if (!currentUser) return [];

    const users = getAllUsers();
    const students = [];

    for (const uid in users) {
      if (users[uid].referredBy === currentUser.referralCode) {
        students.push(users[uid]);
      }
    }

    return students.sort((a, b) => new Date(b.joinedDate) - new Date(a.joinedDate));
  }

  // ============================================
  // CALCULATE TEAM XP
  // ============================================
  function calculateTeamXP(userId = null) {
    const students = getDirectStudents(userId);
    return students.reduce((total, student) => {
      return total + (student.personalXP || 0);
    }, 0);
  }

  // ============================================
  // CALCULATE LINEAGE XP (Recursive)
  // ============================================
  function calculateLineageXP(userId = null) {
    const currentUser = userId ? getUserDataByCode(userId) : getUserData();
    if (!currentUser) return 0;

    let totalXP = 0;
    const students = getDirectStudents(currentUser.userId);

    for (const student of students) {
      totalXP += (student.personalXP || 0);
      // Recursively get their students' XP
      totalXP += calculateLineageXP(student.userId);
    }

    return totalXP;
  }

  // ============================================
  // UPDATE USER XP
  // ============================================
  function updateUserXP(xpAmount) {
    const user = getUserData();
    if (!user) return;

    user.personalXP = (user.personalXP || 0) + xpAmount;
    user.currentBelt = getCurrentBelt();
    saveUserData(user);

    // Update team XP for referrer
    if (user.referredBy) {
      const referrer = getUserDataByCode(user.referredBy);
      if (referrer) {
        referrer.teamXP = calculateTeamXP(referrer.userId);
        saveUserData(referrer);
      }
    }
  }

  // ============================================
  // GET GYM STATS
  // ============================================
  function getGymStats(userId = null) {
    const user = userId ? getUserDataByCode(userId) : getUserData();
    if (!user) return null;

    const students = getDirectStudents(user.userId);
    const teamXP = calculateTeamXP(user.userId);
    const lineageXP = calculateLineageXP(user.userId);

    return {
      gymName: user.gymName || `${user.referralCode}'s Gym`,
      gymMotto: user.gymMotto || null,
      studentsCount: students.length,
      lineageCount: user.lineageCount || 0,
      teamXP: teamXP,
      lineageXP: lineageXP,
      personalXP: user.personalXP || 0,
      currentBelt: user.currentBelt || 'White',
      joinedDate: user.joinedDate,
      students: students
    };
  }

  // ============================================
  // GET LEADERBOARD
  // ============================================
  function getLeaderboard(type = 'teamXP', limit = 100) {
    const users = getAllUsers();
    const gyms = [];

    for (const userId in users) {
      const user = users[userId];
      const stats = getGymStats(user.userId);

      if (stats && stats.studentsCount > 0) {
        gyms.push({
          userId: user.userId,
          gymName: stats.gymName,
          referralCode: user.referralCode,
          studentsCount: stats.studentsCount,
          teamXP: stats.teamXP,
          lineageXP: stats.lineageXP,
          currentBelt: stats.currentBelt
        });
      }
    }

    // Sort by type
    if (type === 'teamXP') {
      gyms.sort((a, b) => b.teamXP - a.teamXP);
    } else if (type === 'lineageXP') {
      gyms.sort((a, b) => b.lineageXP - a.lineageXP);
    } else if (type === 'students') {
      gyms.sort((a, b) => b.studentsCount - a.studentsCount);
    }

    return gyms.slice(0, limit);
  }

  // ============================================
  // GET USER RANK
  // ============================================
  function getUserRank(type = 'teamXP') {
    const leaderboard = getLeaderboard(type, 1000);
    const user = getUserData();
    if (!user) return null;

    const rank = leaderboard.findIndex(gym => gym.userId === user.userId);
    return rank >= 0 ? rank + 1 : null;
  }

  // ============================================
  // SET GYM NAME
  // ============================================
  function setGymName(gymName) {
    const user = getUserData();
    if (!user) return false;

    user.gymName = gymName;
    saveUserData(user);
    return true;
  }

  // ============================================
  // SET GYM MOTTO
  // ============================================
  function setGymMotto(motto) {
    const user = getUserData();
    if (!user) return false;

    user.gymMotto = motto;
    saveUserData(user);
    return true;
  }

  // ============================================
  // SYNC XP FROM LOCALSTORAGE
  // ============================================
  function syncXPFromLocalStorage() {
    const totalXP = parseInt(localStorage.getItem('totalXP') || '0');
    const user = getUserData();
    if (user && user.personalXP !== totalXP) {
      const xpDiff = totalXP - (user.personalXP || 0);
      if (xpDiff > 0) {
        updateUserXP(xpDiff);
      }
    }
  }

  // ============================================
  // INITIALIZE LINEAGE SYSTEM
  // ============================================
  function initializeLineageSystem() {
    // Check for referral in URL
    const referrerCode = getReferrerFromURL();
    if (referrerCode) {
      trackReferralOnStart();
    }

    // Sync XP periodically
    syncXPFromLocalStorage();

    // Update user's belt
    const user = getUserData();
    if (user) {
      user.currentBelt = getCurrentBelt();
      saveUserData(user);
    }
  }

  // ============================================
  // PUBLIC API
  // ============================================
  window.LineageSystem = {
    generateReferralCode,
    getUserReferralCode,
    createReferralLink,
    getReferrerFromURL,
    trackReferralOnStart,
    getUserData,
    getUserDataByCode,
    getDirectStudents,
    calculateTeamXP,
    calculateLineageXP,
    updateUserXP,
    getGymStats,
    getLeaderboard,
    getUserRank,
    setGymName,
    setGymMotto,
    syncXPFromLocalStorage,
    initializeLineageSystem
  };

  // ============================================
  // AUTO-INITIALIZE
  // ============================================
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeLineageSystem);
  } else {
    initializeLineageSystem();
  }

})();


